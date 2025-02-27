from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substring = ''.join([char for char in s[1:7] if char.isalpha()])
    palindromes = set()
    for i in range(4, len(substring) + 1):
        perm = set(permutations(substring, i))
        for p in perm:
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes