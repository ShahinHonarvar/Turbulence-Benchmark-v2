from itertools import permutations

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[4:9] if c.isalpha()]
    palindromes = set()
    for length in range(6, len(chars) + 1):
        for perm in permutations(chars, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes