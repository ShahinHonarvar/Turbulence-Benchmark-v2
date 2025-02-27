from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[:7] if c.isalpha())).lower()
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes