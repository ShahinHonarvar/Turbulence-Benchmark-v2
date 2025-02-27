from itertools import permutations

def palindromes_between_indices(string):
    letters = []
    for i in range(2, 7):
        if i < len(string) and string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(4, len(letters) + 1):
        for item in permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1]:
                result.add(word)
    return result