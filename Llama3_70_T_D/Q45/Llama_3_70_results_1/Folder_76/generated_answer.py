from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    chars = [c for c in s[1:5] if c.isalpha()]
    palindromes = set()
    for p in permutations(chars, 4):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes