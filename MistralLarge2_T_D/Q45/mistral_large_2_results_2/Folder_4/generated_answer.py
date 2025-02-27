from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:10]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(7, len(s) + 1):
        for perm in permutations(s, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes