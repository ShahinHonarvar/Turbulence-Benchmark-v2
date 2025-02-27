from itertools import permutations

def palindromes_between_indices(string):
    letters = []
    for i in range(2, 8):
        if ord('a') <= ord(string[i].lower()) <= ord('z'):
            letters.append(string[i].lower())
    result = set()
    for i in range(6, len(letters) + 1):
        for item in permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1]:
                result.add(word)
    return result