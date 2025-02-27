from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    sub = ''.join(filter(str.isalpha, s[6:10])).lower()
    palindromes = set()
    for length in range(4, len(sub) + 1):
        for perm in permutations(sub, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes