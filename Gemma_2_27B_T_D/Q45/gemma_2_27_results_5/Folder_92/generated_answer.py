from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c for c in s[4:8] if c.isalpha())).lower()
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes