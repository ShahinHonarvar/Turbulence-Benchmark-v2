from itertools import permutations, combinations, chain

def palindromes_between_indices(s):
    permutations_set = set(map(str, chain.from_iterable(map(combinations, set(s[:4]), range(4)))))
    palindromes = set(filter(lambda x: len(set(x)) < 4, permutations_set))
    palindromes = set(map(str.lower, palindromes))
    return palindromes