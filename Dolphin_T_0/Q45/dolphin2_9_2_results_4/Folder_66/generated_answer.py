from itertools import permutations, chain

def palindromes_between_indices(s):
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 5:
        return set()
    palindromes = set()
    combinations = chain.from_iterable((permutations(letters, r) for r in range(5, len(letters) + 1)))
    for subset in combinations:
        if subset == subset[::-1]:
            palindromes.add(''.join(subset))
    return palindromes