from itertools import permutations, chain
    import re

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    letters = chain.from_iterable(permutations(s[2:8]))
    palindromes = (''.join(filter(str.isalpha, p)).lower() for p in letters if len(p) >= 6)
    palindromes = filter(is_palindrome, palindromes)
    return set(palindromes)