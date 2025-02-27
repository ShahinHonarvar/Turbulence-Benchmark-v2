from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c for c in s[1:7] if c.isalpha()])
    letters_lower = letters.lower()
    length = len(letters)
    palindromes = set()
    if length < 7:
        return palindromes
    for p in permutations(letters_lower, length):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 7:
            palindromes.add(word)
    return palindromes