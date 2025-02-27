from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()[4:7]
    result = set()
    for n in range(3, len(s) + 1):
        for p in permutations(s, n):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result