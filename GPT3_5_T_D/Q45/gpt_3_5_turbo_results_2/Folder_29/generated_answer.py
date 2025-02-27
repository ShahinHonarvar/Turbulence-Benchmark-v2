import itertools
    import string

def palindromes_between_indices(s):
    letters = [c.lower() for c in s if c.isalpha()]
    if len(letters) < 8:
        return set()
    palindromes = set()
    for p in itertools.product(letters, repeat=8):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes