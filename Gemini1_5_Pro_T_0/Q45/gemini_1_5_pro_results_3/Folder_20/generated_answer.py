from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    s = string[2:9].lower()
    for i in range(4, len(s) + 1):
        for p in permutations(s, i):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result