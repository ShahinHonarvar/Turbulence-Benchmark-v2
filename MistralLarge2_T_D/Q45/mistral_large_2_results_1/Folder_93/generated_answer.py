import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:8] if c.isalpha()]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for perm in itertools.permutations(letters, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes