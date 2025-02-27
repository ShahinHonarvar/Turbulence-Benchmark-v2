from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substring = ''.join([ch for ch in s[:7] if ch.isalpha()])
    palindromes = set()
    for length in range(4, len(substring) + 1):
        for p in set(permutations(substring, length)):
            w = ''.join(p)
            if w == w[::-1]:
                palindromes.add(w)
    return palindromes