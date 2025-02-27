import itertools

def palindromes_between_indices(s):
    letters = ''.join((s[i] for i in range(8)))
    return {''.join(i).lower() for i in itertools.chain(*[itertools.permutations(letters, l) for l in range(4, len(letters) + 1)]) if i == i[::-1] and i[0] in letters}