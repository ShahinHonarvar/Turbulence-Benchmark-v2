from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7].lower()
    characters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(4, len(characters) + 1):
        for p in permutations(characters, length):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes