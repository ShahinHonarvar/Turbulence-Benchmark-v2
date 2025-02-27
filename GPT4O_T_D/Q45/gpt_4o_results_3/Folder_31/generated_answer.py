from itertools import permutations

def palindromes_between_indices(s):
    s_sub = ''.join([c.lower() for i, c in enumerate(s) if 1 <= i <= 8 and c.isalpha()])
    palindromes = set()
    for length in range(6, len(s_sub) + 1):
        for perm in set(permutations(s_sub, length)):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes