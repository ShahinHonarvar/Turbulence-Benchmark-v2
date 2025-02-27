import itertools

def palindromes_between_indices(string):
    letters = [string[i].lower() for i in range(4, 7) if string[i].isalpha()]
    permutations = set([''.join(p) for i in range(3, len(letters) + 1) for p in itertools.permutations(letters, i)])
    return set([p for p in permutations if p == p[::-1] and len(p) > 2])