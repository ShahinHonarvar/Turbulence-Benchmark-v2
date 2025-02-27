from itertools import permutations

def palindromes_between_indices(text):
    text = text.lower()
    letters = [char for char in text if char.isalpha() and text.index(char) in range(8)]
    if not letters or len(letters) < 6:
        return set()
    permutations_of_letters = set([''.join(p) for p in permutations(letters)])
    return {word for word in permutations_of_letters if word == word[::-1] and len(word) >= 6}