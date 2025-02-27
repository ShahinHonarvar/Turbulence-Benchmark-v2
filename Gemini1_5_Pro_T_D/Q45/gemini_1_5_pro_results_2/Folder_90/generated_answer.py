from itertools import permutations

def palindromes_between_indices(string):
    letters = ''
    for i in range(6):
        if string[i].isalpha():
            letters += string[i].lower()
    result = set()
    if len(letters) < 4:
        return result
    for i in range(4, len(letters) + 1):
        for item in permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1]:
                result.add(word)
    return result