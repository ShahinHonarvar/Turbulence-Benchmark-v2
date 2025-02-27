from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c for c in s[1:7] if c.isalpha()])
    if len(set(letters.lower())) < 7:
        return set()
    palindromes = set()
    for p in permutations(letters, len(letters)):
        word = ''.join(p)
        if word.lower() == word.lower()[::-1] and len(word) >= 7:
            palindromes.add(word)
    return palindromes