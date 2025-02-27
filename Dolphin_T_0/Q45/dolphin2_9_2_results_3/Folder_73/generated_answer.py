from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:7] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters, 3):
        if p == p[::-1]:
            palindromes.add(''.join(p))
    return palindromes