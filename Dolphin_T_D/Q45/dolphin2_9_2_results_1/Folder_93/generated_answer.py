import itertools

def palindromes_between_indices(s):
    letters = ''.join(sorted([c.lower() for c in s[2:7]]))
    return {word for word in itertools.product(letters, repeat=6) if word == word[::-1]}