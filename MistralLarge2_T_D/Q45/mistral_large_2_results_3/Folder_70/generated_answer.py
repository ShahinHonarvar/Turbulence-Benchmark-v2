from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[1:7])).lower()
    palindromes = set()
    for length in range(4, len(substring) + 1):
        for p in permutations(substring, length):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes