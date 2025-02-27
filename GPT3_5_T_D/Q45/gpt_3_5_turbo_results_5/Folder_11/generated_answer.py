import itertools

def palindromes_between_indices(string):
    substring = string[3:8]
    permutations = [''.join(p) for p in itertools.permutations(substring)]
    palindromes = set(filter(lambda x: x.lower() == x[::-1].lower() and len(x) >= 4, permutations))
    return palindromes