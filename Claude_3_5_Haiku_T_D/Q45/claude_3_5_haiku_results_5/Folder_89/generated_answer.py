from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:10] if c.isalpha()]
    if len(letters) < 6:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters)):
        for length in range(6, len(perm) + 1):
            for start in range(len(perm) - length + 1):
                subset = perm[start:start + length]
                if len(subset) >= 6:
                    for p in [subset, subset[::-1]]:
                        candidate = ''.join(p)
                        if candidate == candidate[::-1]:
                            unique_palindromes.add(candidate)
    return unique_palindromes