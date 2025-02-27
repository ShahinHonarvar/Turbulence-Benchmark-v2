from itertools import permutations, chain

def palindromes_between_indices(s):
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 6:
        return set()
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for subset in chain.from_iterable(permutations(letters, r)):
            for p in subset:
                if ''.join(list(p)).lower() == ''.join(list(p)[::-1]).lower():
                    palindromes.add(''.join(list(p)).lower())
    return palindromes