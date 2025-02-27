from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    chars = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(3, len(chars) + 1):
        for perm in permutations(chars, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes