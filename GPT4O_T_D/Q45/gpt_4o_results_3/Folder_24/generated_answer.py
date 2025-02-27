from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for l in range(4, len(letters) + 1):
        for perm in permutations(letters, l):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes