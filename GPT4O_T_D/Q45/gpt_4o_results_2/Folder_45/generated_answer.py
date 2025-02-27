from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:10]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    if len(s) < 4:
        return palindromes
    for length in range(4, len(s) + 1):
        for perm in set(permutations(s, length)):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes