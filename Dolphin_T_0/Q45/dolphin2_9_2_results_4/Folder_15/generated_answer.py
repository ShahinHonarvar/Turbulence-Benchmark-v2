import itertools

def palindromes_between_indices(s):
    letters = [c for c in sorted(set(s[1:3])) if c.isalpha()]
    palindromes = set()
    for length in range(3, len(s[1:3]) + 1):
        for p in itertools.permutations(letters, length):
            pal = ''.join(p)
            if pal == pal[::-1]:
                palindromes.add(pal.lower())
    return palindromes