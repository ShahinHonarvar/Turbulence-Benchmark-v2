from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[4:8] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters, 4):
        if ''.join(p) == ''.join(p)[::-1]:
            palindromes.add(''.join(p).lower())
    return palindromes