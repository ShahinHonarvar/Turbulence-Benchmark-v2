from itertools import permutations, combinations

def palindromes_between_indices(s):
    s = s[3:6].lower()
    result = set()
    for r in range(3, len(s) + 1):
        for c in combinations(s, r):
            for p in permutations(c):
                word = ''.join(p)
                if word == word[::-1]:
                    result.add(word)
    return result