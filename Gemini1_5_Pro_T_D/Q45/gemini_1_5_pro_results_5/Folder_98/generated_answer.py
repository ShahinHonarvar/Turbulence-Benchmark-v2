from itertools import permutations

def palindromes_between_indices(string):
    letters = []
    for i in range(3, 6):
        if string[i].isalpha():
            letters.append(string[i].lower())
    if len(letters) == 0:
        return set()
    result = set()
    for i in range(4, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result