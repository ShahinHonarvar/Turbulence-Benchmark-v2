from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    s = string[2:8].lower()
    letters = [char for char in s if char.isalpha()]
    if len(letters) < 3:
        return result
    for i in range(3, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result