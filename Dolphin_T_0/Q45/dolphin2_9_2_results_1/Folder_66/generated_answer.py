from itertools import permutations

def palindromes_between_indices(string):
    letter_combinations = [''.join(p) for p in permutations(string.lower(), 5)]
    palindromes = [word for word in letter_combinations if word == word[::-1] and len(word) >= 5]
    return set(palindromes)