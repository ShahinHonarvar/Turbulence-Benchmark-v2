from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    letters = [c for c in s[3:10] if c.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word.lower() == word.lower()[::-1]:
                palindromes.add(word)
    return palindromes