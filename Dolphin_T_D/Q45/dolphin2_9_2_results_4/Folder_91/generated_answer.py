from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:7] if c.isalpha()]
    palindromes = set()
    for l in range(3, len(letters) + 1):
        for p in permutations(letters, l):
            word = ''.join(p).lower()
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes