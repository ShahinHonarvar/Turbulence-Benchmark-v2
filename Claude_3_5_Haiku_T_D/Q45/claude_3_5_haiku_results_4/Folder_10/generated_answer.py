from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:6] if c.isalpha()]
    result = set()
    if len(letters) < 3:
        return result
    for length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for candidate in [''.join(p) for p in [perm, perm[::-1]]]:
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result