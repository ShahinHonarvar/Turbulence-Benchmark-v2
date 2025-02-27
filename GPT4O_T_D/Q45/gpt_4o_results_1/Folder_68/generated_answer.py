from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:9].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for perm in set(permutations(letters, i)):
            joined_perm = ''.join(perm)
            if joined_perm == joined_perm[::-1]:
                palindromes.add(joined_perm)
    return palindromes