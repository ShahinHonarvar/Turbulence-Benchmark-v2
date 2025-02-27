from itertools import permutations

def palindromes_between_indices(string):
    s = string[3:9].lower()
    result = set()
    for i in range(4, len(s) + 1):
        for p in permutations(s, i):
            word = ''.join(p)
            if word == word[::-1] and word.isalpha():
                result.add(word)
    return result