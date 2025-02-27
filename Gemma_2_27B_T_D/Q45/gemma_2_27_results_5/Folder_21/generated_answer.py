from itertools import permutations

def palindromes_between_indices(text):
    letters = [c for c in text[1:9] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p).lower()
        if word == word[::-1] and len(word) >= 7:
            palindromes.add(word)
    return palindromes