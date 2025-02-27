from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    s = string[1:8].lower()
    letters = [l for l in s if l.isalpha()]
    for i in range(5, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result