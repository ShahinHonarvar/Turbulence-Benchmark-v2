import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substring = s[26:91]
    palindromes = set()
    for length in range(27, 59):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if re.fullmatch('[A-Za-z]+', candidate) and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes