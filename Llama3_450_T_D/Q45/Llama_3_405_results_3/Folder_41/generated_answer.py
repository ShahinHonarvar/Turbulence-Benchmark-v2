import itertools

def palindromes_between_indices(s):
    slice_ = s[2:4].lower()
    letters = [c for c in slice_ if c.isalpha()]
    letters_set = set(letters)
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in itertools.permutations(letters_set, r):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes