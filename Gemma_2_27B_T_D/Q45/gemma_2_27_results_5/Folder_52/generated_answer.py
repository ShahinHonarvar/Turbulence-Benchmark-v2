from itertools import permutations

def palindromes_between_indices(text):
    letters = [c for c in text[:8].lower() if c.isalpha()]
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes