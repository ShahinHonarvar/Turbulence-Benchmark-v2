from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[:6].lower() if c.isalpha()))
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes