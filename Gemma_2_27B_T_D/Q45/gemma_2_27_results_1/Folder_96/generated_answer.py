from itertools import permutations

def palindromes_between_indices(text):
    letters = [c for c in text[3:9] if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes