from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:7]
    counter = Counter((char.lower() for char in substring if char.isalpha()))
    palindromes = set()
    for length in range(5, len(substring) + 1):
        for perm in permutations(substring, length):
            candidate = ''.join(perm).lower()
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes