from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    chars = [c for c in s[1:7] if c.isalpha()]
    palindromes = set()
    for p in permutations(chars):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 7:
            palindromes.add(word)
    return palindromes