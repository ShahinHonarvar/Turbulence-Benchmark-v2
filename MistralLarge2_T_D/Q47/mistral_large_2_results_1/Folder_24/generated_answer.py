import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    substring = s[12:93].lower()
    palindromes = set()
    for length in range(42, 78):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if is_palindrome(sub) and re.match('^[a-zA-Z]+$', sub):
                palindromes.add(sub)
    return palindromes