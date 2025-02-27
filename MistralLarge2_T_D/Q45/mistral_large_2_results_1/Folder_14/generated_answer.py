from itertools import permutations

def palindromes_between_indices(s):
    chars = [c for c in s[4:6] if c.isalpha()]
    chars = [c.lower() for c in chars]
    palindromes = set()
    for length in range(3, len(chars) + 1):
        for p in permutations(chars, length):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes