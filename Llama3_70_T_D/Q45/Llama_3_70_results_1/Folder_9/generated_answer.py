from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = [c for c in s if c.isalpha()]
    letters_set = set(letters)
    palindromes = set()
    if len(letters_set) < 4:
        return palindromes
    for perm in permutations(letters_set, 7):
        if perm == perm[::-1]:
            palindromes.add(''.join(perm))
    return palindromes