from itertools import permutations

def palindromes_between_indices(s):
    chars = [c for c in s[:7].lower() if c.isalpha()]
    perms = set((''.join(p) for p in permutations(chars, len(chars))))
    palindromes = set()
    for perm in perms:
        for i in range(len(perm)):
            for j in range(i + 7, len(perm) + 1):
                substr = perm[i:j]
                if substr == substr[::-1] and len(substr) >= 7:
                    palindromes.add(substr)
    return palindromes