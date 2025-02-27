from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:8]
    letters = [c.lower() for c in substring if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        if len(perm) >= 6 and perm == perm[::-1]:
            palindromes.add(''.join(perm))
    return palindromes