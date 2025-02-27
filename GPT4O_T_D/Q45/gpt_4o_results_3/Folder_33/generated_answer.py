from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substr = s[7:10].lower()
    chars = [c for c in substr if c.isalpha()]
    if len(chars) < 4:
        return set()
    palindromes = set()
    for length in range(4, len(chars) + 1):
        for perm in permutations(chars, length):
            if ''.join(perm) == ''.join(perm)[::-1]:
                palindromes.add(''.join(perm))
    return palindromes