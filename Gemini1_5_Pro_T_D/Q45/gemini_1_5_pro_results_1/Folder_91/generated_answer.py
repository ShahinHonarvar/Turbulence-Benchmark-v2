from itertools import permutations

def palindromes_between_indices(string):
    s = set()
    for p in permutations(string[2:7]):
        word = ''.join(p).lower()
        if len(word) >= 3 and word == word[::-1]:
            s.add(word)
    return s