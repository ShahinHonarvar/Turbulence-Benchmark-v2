import itertools
    import re

def palindromes_between_indices(string):
    letters = re.findall('[a-zA-Z]', string[1:8])
    perms = set(itertools.permutations(letters, len(string[1:8])))
    palindromes = set()
    for perm in perms:
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes