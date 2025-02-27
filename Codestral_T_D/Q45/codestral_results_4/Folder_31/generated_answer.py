from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:9].lower()
    palindromes = set()
    for length in range(6, len(s) + 1):
        for p in permutations(s, length):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes