from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[1:8] if c.isalpha()]
    letters_lower = [c.lower() for c in letters]
    palindromes = set()
    for length in range(7, len(letters_lower) + 1):
        for perm in permutations(letters_lower, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes