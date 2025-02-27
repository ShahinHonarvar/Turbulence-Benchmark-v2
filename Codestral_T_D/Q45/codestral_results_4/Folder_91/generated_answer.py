from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:7].lower()
    results = set()
    for p in range(3, len(s) + 1):
        for perm in permutations(s, p):
            word = ''.join(perm)
            if word == word[::-1]:
                results.add(word)
    return results