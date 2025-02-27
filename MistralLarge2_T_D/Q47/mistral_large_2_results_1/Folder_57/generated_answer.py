import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    substring = s[16:95].lower()
    palindromes = set()
    for length in range(39, 53):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate) and re.match('^[a-z]+$', candidate):
                palindromes.add(candidate)
    return palindromes