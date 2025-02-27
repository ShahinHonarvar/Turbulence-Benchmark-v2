import itertools

def palindromes_between_indices(s):
    subset = ''.join([c for c in s[2:7] if c.isalpha()]).lower()
    result = set()
    for length in range(3, len(subset) + 1):
        for combo in itertools.permutations(subset, length):
            if combo == combo[::-1]:
                result.add(''.join(combo))
    return result