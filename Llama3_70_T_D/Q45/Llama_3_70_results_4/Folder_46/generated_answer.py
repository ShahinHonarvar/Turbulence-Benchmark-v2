from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10] if c.isalpha()]
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1] and len(word) >= 6:
                palindromes.add(word)
    return palindromes