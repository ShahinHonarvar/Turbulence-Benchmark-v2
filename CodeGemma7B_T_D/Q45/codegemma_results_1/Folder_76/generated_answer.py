from itertools import permutations
from string import ascii_lowercase

def palindromes_between_indices(text):
    required_letters = {letter.lower() for letter in text[1:5]}
    all_palindromes = set()
    for p in permutations(ascii_lowercase):
        current_set = set()
        for word in p:
            if word in required_letters:
                current_set.add(word)
        if len(current_set) >= 4:
            palindromes = [''.join(p) for p in permutations(current_set)]
            all_palindromes |= set(palindromes)
    return all_palindromes