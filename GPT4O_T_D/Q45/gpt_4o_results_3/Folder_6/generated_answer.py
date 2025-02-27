from itertools import permutations

def palindromes_between_indices(s):
    s = s[:8].lower()
    useful_chars = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(4, len(useful_chars) + 1):
        for perm in permutations(useful_chars, i):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes