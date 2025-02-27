from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[3:8] if c.isalpha()]
    palindromes = set()
    for l in range(4, len(letters) + 1):
        for p in permutations(letters, l):
            pal = ''.join(p)
            if pal == pal[::-1]:
                palindromes.add(pal)
    return palindromes