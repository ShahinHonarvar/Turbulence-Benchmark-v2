from itertools import permutations

def palindromes_between_indices(s):
    substring = s[:7].lower()
    letters = [c for c in substring if c.isalpha()]
    results = set()
    for perm in permutations(letters):
        for length in range(3, len(letters) + 1):
            for start in range(len(perm) - length + 1):
                candidate = ''.join(perm[start:start + length])
                if candidate == candidate[::-1]:
                    results.add(candidate)
    return results