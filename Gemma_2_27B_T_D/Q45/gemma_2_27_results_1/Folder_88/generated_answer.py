from itertools import permutations

def palindromes_between_indices(text):
    letters = [char for char in text[3:8] if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if word.lower() == word.lower()[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes