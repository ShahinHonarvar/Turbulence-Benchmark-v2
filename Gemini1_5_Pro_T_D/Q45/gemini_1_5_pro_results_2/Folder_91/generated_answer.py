from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for i in range(3, 7):
        for p in permutations(string[2:7], i):
            word = ''.join(p).lower()
            if word == word[::-1] and len(word) >= 3:
                result.add(word)
    return result