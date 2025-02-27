from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:8].lower()
    result = set()
    for i in range(5, len(s) + 1):
        for p in permutations(s, i):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result