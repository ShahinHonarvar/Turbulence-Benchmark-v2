from itertools import permutations

def palindromes_between_indices(string):
    letters = []
    for i in range(0, 8):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for length in range(6, len(letters) + 1):
        for candidate in permutations(letters, length):
            word = ''.join(candidate)
            if word == word[::-1]:
                result.add(word)
    return result