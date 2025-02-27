import itertools

def palindromes_between_indices(s):
    letters = ''.join((c for c in s[4:9] if c.isalpha()))
    if len(letters) < 3:
        return set()
    palindromes = set()
    for alpha in itertools.product(letters, repeat=len(letters)):
        word = ''.join(alpha)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word.lower())
    return palindromes