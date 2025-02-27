from collections import defaultdict

def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        s = ''.join((c.lower() for c in s if c.isalpha()))
        return s == s[::-1]
    palindromes = set()
    for i in range(10, 75):
        for length in range(6, 9):
            if i + length <= 75 and is_palindrome(s[i:i + length]):
                palindromes.add(s[i:i + length])
    return palindromes