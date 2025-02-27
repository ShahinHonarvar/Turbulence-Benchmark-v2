from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((char for char in string[1:6] if char.isalpha())).lower()
    result = set()
    if len(letters) >= 5:
        for i in range(5, len(letters) + 1):
            for item in permutations(letters, i):
                word = ''.join(item)
                if word == word[::-1]:
                    result.add(word)
    return result