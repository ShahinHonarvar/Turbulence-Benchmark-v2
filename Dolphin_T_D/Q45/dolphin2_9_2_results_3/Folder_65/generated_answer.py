import itertools
    from string import ascii_lowercase

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[:7].lower()
    letters = [c for c in ascii_lowercase if c in s]
    return set(filter(is_palindrome, map(''.join, itertools.product(*map(lambda l: l * 5, letters)))))