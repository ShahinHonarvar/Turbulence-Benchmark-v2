import itertools

def palindromes_between_indices(s):
    substr = s[2:5].lower()
    letters = [c for c in substr if c.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in itertools.permutations(letters, r):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes