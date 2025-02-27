from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((char for char in string[1:3] if char.isalpha())).lower()
    pals = set()
    for i in range(3, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                pals.add(word)
    return pals