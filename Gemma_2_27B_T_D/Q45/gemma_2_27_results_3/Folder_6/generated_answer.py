from itertools import permutations

def palindromes_between_indices(text):
    s = text[0:8]
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes