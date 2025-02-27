from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7]
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for p in permutations(letters, len(letters)):
        word = ''.join(p)
        if word == word.lower() and len(word) >= 6:
            palindromes.add(word)
    return palindromes