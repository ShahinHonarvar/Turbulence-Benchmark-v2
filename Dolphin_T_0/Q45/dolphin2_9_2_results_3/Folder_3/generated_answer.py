from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[6:10]]
    palindromes = set()
    for p in permutations(letters, 3):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes