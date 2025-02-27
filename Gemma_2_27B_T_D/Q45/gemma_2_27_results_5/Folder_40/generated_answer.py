from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[4:10] if c.isalpha())).lower()
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 7:
            palindromes.add(word)
    return palindromes