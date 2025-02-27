from itertools import permutations

def palindromes_between_indices(string):
    string = string[0:9].lower()
    result = set()
    for i in range(7, len(string) + 1):
        for p in permutations(string, i):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result