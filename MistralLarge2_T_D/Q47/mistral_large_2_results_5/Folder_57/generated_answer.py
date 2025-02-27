import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[16:95].lower()
    palindromes = set()
    for length in range(39, 53):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if is_palindrome(sub) and re.match('^[a-z]*$', sub):
                palindromes.add(sub)
    return palindromes