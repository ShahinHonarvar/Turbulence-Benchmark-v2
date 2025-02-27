from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substring = s[2:4]
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for perm in permutations(substring, length):
            if ''.join(perm) == ''.join(perm)[::-1]:
                palindromes.add(''.join(perm))
    return palindromes