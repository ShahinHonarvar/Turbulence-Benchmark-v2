from itertools import permutations, chain

def palindromes_between_indices(s):
    pal = set()
    elements = [x for x in s[2:8] if x.isalpha()]
    for p in chain.from_iterable((permutations(elements, r) for r in range(3, len(elements) + 1))):
        if ''.join(p).lower() == ''.join(p[::-1]).lower():
            pal.add(''.join(p))
    return pal