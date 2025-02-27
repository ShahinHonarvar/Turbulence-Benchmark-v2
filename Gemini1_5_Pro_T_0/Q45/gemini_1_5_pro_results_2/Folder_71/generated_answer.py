from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((c for c in string[1:4] if c.isalpha())).lower()
    result = set()
    if len(letters) >= 4:
        for i in range(4, len(letters) + 1):
            for p in set(permutations(letters, i)):
                candidate = ''.join(p)
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result