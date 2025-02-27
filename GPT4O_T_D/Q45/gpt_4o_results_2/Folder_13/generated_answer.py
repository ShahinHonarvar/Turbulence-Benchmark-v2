from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[3:10].lower()
    filtered_chars = ''.join((c for c in substring if c.isalpha()))
    palindromes = set()
    for length in range(5, len(filtered_chars) + 1):
        for perm in set(permutations(filtered_chars, length)):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes