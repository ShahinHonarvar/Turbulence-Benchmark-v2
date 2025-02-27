from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    substr = s[1:9]
    letters = [c.lower() for c in substr if c.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes