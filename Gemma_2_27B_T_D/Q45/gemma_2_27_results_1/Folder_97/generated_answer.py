from itertools import permutations

def palindromes_between_indices(text):
    letters = [c for c in text[:5] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters, 3):
        word = ''.join(p).lower()
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes