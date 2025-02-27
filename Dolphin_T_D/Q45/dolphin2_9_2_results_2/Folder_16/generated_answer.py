from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[6:10] if c.isalpha()))
    palindromes = set()
    if len(letters) < 5:
        return palindromes
    for p in permutations(letters, len(letters)):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes