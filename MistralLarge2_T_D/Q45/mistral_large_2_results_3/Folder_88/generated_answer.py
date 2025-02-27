from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join([c for c in s[3:8] if c.isalpha()]).lower()
    palindromes = set()
    for length in range(6, len(substring) + 1):
        for perm in permutations(substring, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes