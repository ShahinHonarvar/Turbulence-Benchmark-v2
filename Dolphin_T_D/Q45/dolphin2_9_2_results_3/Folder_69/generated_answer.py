from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 4:
        return set()
    letters = [c for c in s[0:4] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters, len(letters)):
        word = ''.join(p)
        if len(word) >= 4 and word == word.lower()[::-1]:
            palindromes.add(word)
    return palindromes