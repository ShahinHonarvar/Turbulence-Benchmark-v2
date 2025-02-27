from itertools import permutations

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[1:7] if c.isalpha()]
    perms = [''.join(p) for p in permutations(chars, len(chars))]
    palindromes = set()
    for perm in perms:
        for i in range(len(perm) - 5):
            for j in range(i + 6, len(perm) + 1):
                substr = perm[i:j]
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes