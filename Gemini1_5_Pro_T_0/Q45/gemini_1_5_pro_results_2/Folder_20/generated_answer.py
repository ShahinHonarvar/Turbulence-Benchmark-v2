from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    s = string[2:9].lower()
    letters = [char for char in s if char.isalpha()]
    if len(letters) >= 4:
        for i in range(4, len(letters) + 1):
            for p in permutations(letters, i):
                word = ''.join(p)
                if word == word[::-1]:
                    result.add(word)
    return result