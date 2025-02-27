from itertools import permutations 
from collections import defaultdict

def palindromes_between_indices(text):

    def is_palindrome(word):
        return word == word[::-1]
    letters = defaultdict(list)
    for index, char in enumerate(text):
        if index >= 2 and index <= 8:
            letters[char.lower()].append(index)
    palindromes = set()
    for char, indices in letters.items():
        for indices_permutation in permutations(indices):
            word = ''.join((text[i] for i in indices_permutation))
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes