from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(s):
    s = s[2:7].lower()
    s = ''.join((c for c in s if c in ascii_lowercase))
    s_set = set(s)
    if len(s_set) < 2:
        return set()
    palindromes = set()
    for length in range(4, len(s) + 1):
        for p in permutations(s, length):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes