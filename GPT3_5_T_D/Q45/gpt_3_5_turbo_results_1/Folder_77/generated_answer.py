import itertools
    import re

def palindromes_between_indices(string):
    pattern = re.compile('[a-zA-Z]')
    letters = pattern.findall(string[4:7])
    letters = ''.join(letters)
    perms = set(itertools.permutations(letters, len(letters)))
    palindromes = set()
    for perm in perms:
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes