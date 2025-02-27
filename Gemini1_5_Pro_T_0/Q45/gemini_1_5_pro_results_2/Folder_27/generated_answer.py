from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    s = string[2:9].lower()
    letters = [char for char in s if char.isalpha()]
    if len(letters) < 6:
        return result
    for i in range(6, len(letters) + 1):
        for item in permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1]:
                result.add(word)
    return result