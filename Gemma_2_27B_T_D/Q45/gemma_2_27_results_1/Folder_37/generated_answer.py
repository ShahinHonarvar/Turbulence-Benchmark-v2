from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:5]))
    return {p.lower() for p in map(''.join, permutations(letters)) if len(p) >= 5 and p == p[::-1]}