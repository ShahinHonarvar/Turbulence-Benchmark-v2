from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[:5] if c.isalpha()))
    result = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result