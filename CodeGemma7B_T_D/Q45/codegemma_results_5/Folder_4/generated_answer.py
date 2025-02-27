from itertools import permutations
import re

def palindromes_between_indices(string):
    letters = [c for c in string[3:10] if c.isalpha()]
    palindromes = set()
    for permutation in permutations(letters):
        palindrome = ''.join(list(permutation))
        if palindrome.__eq__(palindrome[::-1]) and len(palindrome) >= 7:
            palindromes.add(palindrome.lower())
    return palindromes