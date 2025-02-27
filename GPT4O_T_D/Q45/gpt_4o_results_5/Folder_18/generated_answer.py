from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 7:
        return set()
    s = s[1:7].lower()
    chars = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for length in range(3, len(chars) + 1):
        for perm in set(permutations(chars, length)):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes