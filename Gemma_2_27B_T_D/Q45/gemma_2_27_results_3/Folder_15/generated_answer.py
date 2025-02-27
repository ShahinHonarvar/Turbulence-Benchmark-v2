from itertools import permutations

def palindromes_between_indices(text):
    letters = [c for c in text[1:3] if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if word.lower() == word.lower()[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes