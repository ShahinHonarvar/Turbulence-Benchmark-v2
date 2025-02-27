import string

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()
    s = ''.join((ch for ch in s if ch.isalpha()))
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 7, len(s) + 1):
            subset = ''.join(sorted(s[i:j]))
            if is_palindrome(subset):
                palindromes.add(subset)
    return palindromes