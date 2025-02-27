from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted((c.lower() for c in string[2:8] if c.isalpha())))
    result = set()
    for i in range(6, len(letters) + 1):
        for p in permutations(letters, i):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result