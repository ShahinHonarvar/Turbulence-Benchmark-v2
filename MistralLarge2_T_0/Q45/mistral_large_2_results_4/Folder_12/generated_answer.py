import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[3:9] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in itertools.permutations(letters, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes