from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    s = string[1:8].lower()
    letters = []
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            letters.append(c)
    for i in range(6, len(letters) + 1):
        for p in permutations(letters, i):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result