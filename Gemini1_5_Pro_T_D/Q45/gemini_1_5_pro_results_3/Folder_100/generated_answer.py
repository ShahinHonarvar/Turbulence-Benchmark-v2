from itertools import permutations

def palindromes_between_indices(string):
    letters = []
    for i in range(6):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(6, len(letters) + 1):
        for item in permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1] and len(word) >= 6:
                result.add(word)
    return result