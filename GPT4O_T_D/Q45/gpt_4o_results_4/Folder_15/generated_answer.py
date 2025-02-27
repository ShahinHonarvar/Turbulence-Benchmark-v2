from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    chars = ''.join(filter(str.isalpha, s[1:3]))
    results = set()
    for length in range(3, len(chars) + 1):
        for perm in permutations(chars, length):
            if ''.join(perm) == ''.join(perm)[::-1]:
                results.add(''.join(perm))
    return results