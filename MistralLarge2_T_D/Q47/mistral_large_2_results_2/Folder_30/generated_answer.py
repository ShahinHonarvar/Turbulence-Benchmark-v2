import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substr = s[14:91]
    palindromes = set()
    for length in range(55, 72):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if re.match('^[A-Za-z]+$', sub) and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes