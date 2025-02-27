from itertools import permutations

def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    s = s.lower()
    letters = ''.join((c for c in s[:8] if c.isalpha()))
    for perm in permutations(letters):
        if perm == perm[::-1] and len(perm) >= 4:
            palindromes.add(''.join(perm))
    return palindromes