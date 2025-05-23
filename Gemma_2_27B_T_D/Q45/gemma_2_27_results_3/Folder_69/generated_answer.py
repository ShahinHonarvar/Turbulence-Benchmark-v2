from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[:4] if c.isalpha()))
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if word.lower() == word.lower()[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes