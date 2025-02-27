import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substring = s[16:78]
    length_range = range(43, 48)
    palindromes = set()
    for length in length_range:
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if re.match('^[A-Za-z]*$', sub) and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes