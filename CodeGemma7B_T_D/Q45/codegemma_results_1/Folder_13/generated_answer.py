from itertools import permutations

def palindromes_between_indices(text):
    first = {i for i in text[3:10].lower() if i in 'abcdefghijklmnopqrstuvwxyz'}
    ps = []
    for p in permutations(first):
        r = ''.join(p)
        if r == r[::-1] and len(r) >= 5:
            ps.append(r)
    return set(ps)