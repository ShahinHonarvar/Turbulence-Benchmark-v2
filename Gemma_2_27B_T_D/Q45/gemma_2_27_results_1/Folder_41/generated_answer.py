from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:4] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p).lower()
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes