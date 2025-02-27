import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[4:8] if c.isalpha()]
    unique_letters = set((c.lower() for c in letters))
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for p in itertools.permutations(unique_letters, length):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes