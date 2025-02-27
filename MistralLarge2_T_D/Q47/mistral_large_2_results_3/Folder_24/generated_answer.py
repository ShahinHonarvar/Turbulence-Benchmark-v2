import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substring = s[12:93]
    palindromes = set()
    for length in range(42, 78):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if re.match('^[A-Za-z]+$', candidate) and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes