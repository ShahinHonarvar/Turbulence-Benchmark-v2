import itertools
    import string as s

def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.isalpha()]
    letters = letters[:4]
    palindromes = set()
    for perm in itertools.permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes