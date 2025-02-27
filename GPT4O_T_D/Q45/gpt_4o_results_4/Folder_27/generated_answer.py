from itertools import permutations

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[2:9] if c.isalpha()]
    unique_perms = set(permutations(chars))
    palindromes = set()
    for perm in unique_perms:
        for length in range(6, len(perm) + 1):
            current_perm = perm[:length]
            if current_perm == current_perm[::-1]:
                palindromes.add(''.join(current_perm))
    return palindromes