from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    s = string[2:9].lower()
    letters = [ch for ch in s if ch.isalpha()]
    if len(letters) < 7:
        return result
    for i in range(7, len(letters) + 1):
        for p in permutations(letters, i):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result