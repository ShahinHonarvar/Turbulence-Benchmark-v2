from itertools import permutations

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[2:8] if c.isalpha()]
    if len(chars) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(chars) + 1):
        for perm in permutations(chars, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes