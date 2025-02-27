from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(w):
        return w == w[::-1]
    s = ''.join(filter(str.isalpha, s[:9]))
    return set(filter(is_palindrome, map(''.join, permutations(s, 7))))