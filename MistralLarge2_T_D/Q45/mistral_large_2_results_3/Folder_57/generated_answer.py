from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[2:6]))
    substring = substring.lower()
    palindromes = set()
    for length in range(5, len(substring) + 1):
        for perm in permutations(substring, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes