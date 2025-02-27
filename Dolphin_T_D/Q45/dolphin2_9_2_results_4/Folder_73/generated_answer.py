from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:7] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for p in permutations(letters, 3):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes