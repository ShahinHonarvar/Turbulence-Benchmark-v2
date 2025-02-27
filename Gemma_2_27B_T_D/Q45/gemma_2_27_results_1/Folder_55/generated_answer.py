from itertools import permutations

def palindromes_between_indices(text):
    letters = [c for c in text[:3] if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm).lower()
        if len(word) >= 3 and word == word[::-1]:
            palindromes.add(word)
    return palindromes