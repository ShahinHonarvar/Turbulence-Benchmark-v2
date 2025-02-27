from itertools import permutations

def palindromes_between_indices(string):
    letters = []
    for i in range(6):
        if string[i].isalpha() and string[i].lower() not in letters:
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) + 1):
        for j in permutations(letters, i):
            word = ''.join(j)
            if len(word) >= 6 and word == word[::-1]:
                result.add(word)
    return result