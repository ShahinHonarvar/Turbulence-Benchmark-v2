from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:7].lower()
    chars = [c for c in substring if c.isalpha()]
    unique_palindromes = set()
    for p in permutations(chars):
        word = ''.join(p)
        if len(word) >= 3 and word == word[::-1]:
            unique_palindromes.add(word)
    return unique_palindromes