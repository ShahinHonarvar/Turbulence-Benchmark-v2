from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[4:10].lower() if c.isalpha()]
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes