import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[1:9] if c.isalpha()]
    perms = itertools.permutations(letters)
    palindromes = set()
    for perm in perms:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes