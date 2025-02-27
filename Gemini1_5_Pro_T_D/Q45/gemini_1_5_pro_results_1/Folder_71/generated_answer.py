from itertools import permutations

def palindromes_between_indices(string):
    letters = []
    for i in range(1, 4):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    if len(letters) > 1:
        for i in range(2, len(letters) + 1):
            for p in permutations(letters, i):
                word = ''.join(p)
                if word == word[::-1] and len(word) >= 4:
                    result.add(word)
    return result