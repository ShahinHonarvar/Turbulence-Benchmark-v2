from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    s = string[4:8].lower()
    for i in range(5, len(s) + 1):
        for p in permutations(s, i):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result