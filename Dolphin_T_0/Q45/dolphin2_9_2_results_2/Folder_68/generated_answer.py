import re

def palindromes_between_indices(string):
    palindromes = set()
    combinations = re.findall('[a-zA-Z]', string[1:9])
    permutations = set((''.join(p) for _ in range(len(combinations)) for p in permutations(combinations, len(combinations))))
    for permutation in permutations:
        if permutation == permutation[::-1] and len(permutation) >= 4:
            palindromes.add(permutation.lower())
    return palindromes