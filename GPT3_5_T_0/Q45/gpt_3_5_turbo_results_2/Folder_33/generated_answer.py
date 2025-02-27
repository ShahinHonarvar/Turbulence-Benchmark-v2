import itertools
    import re

def palindromes_between_indices(string):
    letters = re.findall('[a-zA-Z]', string[7:10])
    permutations = set(itertools.permutations(letters))
    palindromes = set()
    for perm in permutations:
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes