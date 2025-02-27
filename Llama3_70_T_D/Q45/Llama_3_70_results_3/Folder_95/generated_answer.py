from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[7:9] if c.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes