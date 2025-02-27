from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[1:8] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p).lower()
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes