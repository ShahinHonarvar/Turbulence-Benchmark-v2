import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[17:96]
    palindromes = set()
    for length in range(13, 50):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if is_palindrome(sub) and re.match('^[A-Za-z]*$', sub):
                palindromes.add(sub.lower())
    return palindromes