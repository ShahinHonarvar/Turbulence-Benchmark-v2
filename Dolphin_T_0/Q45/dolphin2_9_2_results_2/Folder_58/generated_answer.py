from itertools import permutations
import string

def palindromes_between_indices(s):
    palindromes = set()
    for p in permutations(s[0:7].lower(), 6):
        if p == p[::-1] and ''.join(p).isalpha():
            palindromes.add(''.join(p))
    return palindromes