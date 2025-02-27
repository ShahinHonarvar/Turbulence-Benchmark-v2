import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[:7].lower() if c.isalpha()]
    perms = set(itertools.permutations(letters))
    palindromes = set()
    for perm in perms:
        for length in range(4, len(perm) + 1):
            for i in range(len(perm) - length + 1):
                candidate = ''.join(perm[i:i + length])
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes