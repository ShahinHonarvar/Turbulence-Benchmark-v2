from itertools import permutations

def palindromes_between_indices(text):
    letters = [char for char in text[1:7] if char.isalpha()]
    palindromes = set()
    for permutation in permutations(letters):
        word = ''.join(permutation)
        if word.lower() == word.lower()[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes