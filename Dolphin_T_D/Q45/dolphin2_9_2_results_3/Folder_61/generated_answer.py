from itertools import permutations

def palindromes_between_indices(s):
    s = s[:8].lower()
    result = set()
    for r in range(7, 0, -1):
        for p in permutations(s, r):
            word = ''.join(p)
            if word == word[::-1] and len(word) >= 7:
                result.add(word)
    return result