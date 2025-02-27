from itertools import permutations
from collections import defaultdict

def palindromes_between_indices(text):
    frequencies = defaultdict(int)
    for char in text[6:9]:
        frequencies[char.lower()] += 1
    palindromes = set()
    for permutation in permutations(frequencies.keys()):
        word = ''.join(permutation)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word.lower())
    return palindromes