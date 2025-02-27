import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[:9] if c.isalpha()]
    palindromes = set()
    for p in itertools.permutations(letters, 7):
        if ''.join(p).lower() == ''.join(p[::-1]).lower():
            palindromes.add(''.join(p).lower())
    return palindromes