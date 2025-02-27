from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    mid_chars = ''.join(filter(str.isalpha, s[5:9])).lower()
    palindromes = set()
    for length in range(3, len(mid_chars) + 1):
        for p in permutations(mid_chars, length):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes