from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = [c for c in s if c.isalpha()]
    results = set()
    for i in range(5, len(letters) + 1):
        for perm in set(permutations(letters, i)):
            if perm == perm[::-1]:
                results.add(''.join(perm))
    return results