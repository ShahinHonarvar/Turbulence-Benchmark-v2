from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    string = string[3:8].lower()
    for i in range(6, len(string) + 1):
        for p in permutations(string, i):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result