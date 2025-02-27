import itertools

def palindromes_between_indices(string):
    arrangements = [''.join(p) for p in itertools.permutations(string[1:5])]
    palindromes = {arrangement for arrangement in arrangements if arrangement == arrangement[::-1] and len(arrangement) >= 5}
    return palindromes