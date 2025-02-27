from itertools import permutations

def palindromes_between_indices(text):
    letters = [char for char in text[3:9] if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes