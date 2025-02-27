from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[4:8] if c.isalpha()]
    letters = ''.join(letters).lower()
    if len(letters) < 5:
        return set()
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for p in permutations(letters, length):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes