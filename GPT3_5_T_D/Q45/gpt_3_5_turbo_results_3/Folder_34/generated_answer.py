import itertools
    import string

def palindromes_between_indices(string):
    letters = [letter.lower() for letter in string[5:8] if letter in string.ascii_letters]
    permutations = set(itertools.permutations(letters))
    palindromes = set()
    for perm in permutations:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes