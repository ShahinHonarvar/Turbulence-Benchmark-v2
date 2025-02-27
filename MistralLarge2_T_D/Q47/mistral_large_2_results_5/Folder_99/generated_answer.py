import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substr = s[127:289]
    palindromes = set()
    for length in range(119, 142):
        for start in range(len(substr) - length + 1):
            sub = substr[start:start + length]
            if re.match('^[A-Za-z]+$', sub) and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes