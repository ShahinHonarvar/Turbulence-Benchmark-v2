import itertools

def palindromes_between_indices(string):
    s = string[4:8].lower()
    letters = [char for char in s if char.isalpha()]
    permutations = set([''.join(p) for p in itertools.permutations(letters)])
    palindromes = {word for word in permutations if len(word) >= 5 and word == word[::-1]}
    return palindromes