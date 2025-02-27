import itertools

def palindromes_between_indices(string):
    letters = set([c.lower() for c in string[1:7] if c.isalpha()])
    permutations = itertools.chain.from_iterable((itertools.permutations(letters, r) for r in range(1, len(letters) + 1)))
    return set([''.join(p) for p in permutations if len(''.join(p)) >= 7 and ''.join(p) == ''.join(p)[::-1]])