from functools import reduce
import re

def palindromes_between_indices(string):

    def is_palindrome(s):
        return s == s[::-1]

    def char_to_set(c):
        return set(filter(str.isalpha, c.upper()))

    def combine_sets(s1, s2):
        return s1 | s2 - set('AEIOU')

    def form_palindromes(sets):
        return [''.join(c) for p in sets for c in [p, p[::-1]] if len(c) >= 4 and is_palindrome(c)]
    sets = reduce(combine_sets, map(char_to_set, string[:8]), set())
    palindromes = form_palindromes(sets)
    return set(filter(is_palindrome, palindromes))