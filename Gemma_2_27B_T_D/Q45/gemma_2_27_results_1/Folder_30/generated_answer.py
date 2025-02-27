from itertools import permutations

def palindromes_between_indices(text):
    letters = [char for char in text[0:5] if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm).lower()
        if len(word) >= 4 and word == word[::-1]:
            palindromes.add(word)
    return palindromes