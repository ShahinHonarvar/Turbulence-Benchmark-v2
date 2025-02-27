from itertools import permutations

def palindromes_between_indices(s):
    s = s[:8].lower()
    letters = [c for c in s if c.isalpha()]
    result = set()
    for length in range(6, min(8, len(letters)) + 1):
        for perm in set(permutations(letters, length)):
            if perm == perm[::-1]:
                result.add(''.join(perm))
    return result