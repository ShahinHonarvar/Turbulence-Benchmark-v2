import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[2:9] if c.isalpha()]
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for combination in itertools.permutations(letters, r):
            for p in ''.join(combination).lower().palindrome():
                palindromes.add(p)
    return palindromes