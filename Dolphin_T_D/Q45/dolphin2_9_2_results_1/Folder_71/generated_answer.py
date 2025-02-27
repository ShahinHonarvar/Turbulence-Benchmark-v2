from itertools import permutations
    import re

def palindromes_between_indices(input_string):
    input_string = input_string[1:4]
    letters = [ch for ch in input_string if ch.isalpha()]
    english_letters = set((letter.lower() for letter in letters))
    if len(english_letters) < 2:
        return set()
    length = 4
    while True:
        for p in permutations(english_letters, length):
            word = ''.join(p).lower()
            if word == word[::-1]:
                return set([word])
        length += 1