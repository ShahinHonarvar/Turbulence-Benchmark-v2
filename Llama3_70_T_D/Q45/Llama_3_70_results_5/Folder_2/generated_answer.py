import itertools

def palindromes_between_indices(s):
    s = s[:6].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for r in range(len(letters), 5, -1):
        for perm in itertools.permutations(letters, r):
            perm = ''.join(perm)
            if perm == perm[::-1] and len(perm) >= 6:
                palindromes.add(perm)
    return palindromes