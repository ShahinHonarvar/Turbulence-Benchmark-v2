import itertools

def palindromes_between_indices(string):
    letters = set([x.lower() for x in string[3:8] if x.isalpha()])
    permutations = set([''.join(p) for i in range(1, len(letters) + 1) for p in itertools.permutations(letters, i)])
    return set([x for x in permutations if len(x) >= 5 and x == x[::-1]])