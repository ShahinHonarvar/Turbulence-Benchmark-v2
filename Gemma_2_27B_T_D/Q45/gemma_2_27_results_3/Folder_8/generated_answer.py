from itertools import permutations

def palindromes_between_indices(text):
    letters = sorted([c.lower() for c in text[1:6] if c.isalpha()])
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes