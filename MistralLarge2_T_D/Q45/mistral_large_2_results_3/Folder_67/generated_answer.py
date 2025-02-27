import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:7] if c.isalpha()]
    if len(letters) < 5:
        return set()
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in itertools.permutations(letters, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes