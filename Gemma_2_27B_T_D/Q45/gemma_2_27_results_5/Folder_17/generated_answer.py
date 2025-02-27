from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[2:7] if c.isalpha())).lower()
    palindromes = set()
    for perm in permutations(letters):
        s = ''.join(perm)
        if len(s) >= 4 and s == s[::-1]:
            palindromes.add(s)
    return palindromes