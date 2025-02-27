import itertools

def palindromes_between_indices(string):
    s = string[4:8].lower()
    letters = [ch for ch in s if ch.isalpha()]
    permutations = set([''.join(p) for p in itertools.permutations(letters)])
    return {p for p in permutations if len(p) >= 5 and p == p[::-1]}