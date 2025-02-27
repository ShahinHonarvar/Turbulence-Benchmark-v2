from itertools import permutations

def palindromes_between_indices(text):
    letters = [letter for letter in text[5:10] if letter.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes