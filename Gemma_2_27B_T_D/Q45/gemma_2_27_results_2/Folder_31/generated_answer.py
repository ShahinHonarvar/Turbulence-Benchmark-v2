from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[1:9] if c.isalpha()]
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p).lower()
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes