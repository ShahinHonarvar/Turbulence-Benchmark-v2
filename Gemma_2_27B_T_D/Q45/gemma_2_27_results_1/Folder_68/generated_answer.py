from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[1:9] if c.isalpha())).lower()
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if len(word) >= 4 and word == word[::-1]:
            palindromes.add(word)
    return palindromes