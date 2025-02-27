from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    segment = ''.join((c for c in s[3:8] if c.isalpha()))
    palindromes = set()
    for perm in permutations(segment):
        if perm == perm[::-1] and len(perm) >= 5:
            palindromes.add(''.join(perm))
    return palindromes