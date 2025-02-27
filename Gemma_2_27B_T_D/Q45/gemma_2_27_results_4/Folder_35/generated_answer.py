from itertools import permutations

def palindromes_between_indices(text):
    letters = [letter for letter in text[2:5] if letter.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes