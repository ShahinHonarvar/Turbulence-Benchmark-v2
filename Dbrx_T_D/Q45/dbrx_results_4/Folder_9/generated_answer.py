import re

def palindromes_between_indices(s):
    letters = set('abcdefghijklmnopqrstuvwxyz')
    letter_indices = [i for i, c in enumerate(s[:7]) if c.lower() in letters]
    arrangements = [''.join(c) for c in itertools.permutations((s[i] for i in letter_indices))]
    palindromes = {arr for arr in arrangements if len(arr) >= 7 and arr == arr[::-1]}
    return palindromes