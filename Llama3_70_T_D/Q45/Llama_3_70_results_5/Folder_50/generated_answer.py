from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s[4:9] if c.isalpha()]
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes