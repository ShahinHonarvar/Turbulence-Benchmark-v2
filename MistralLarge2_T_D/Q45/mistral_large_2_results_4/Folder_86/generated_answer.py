from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[6:10].lower() if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            pal = ''.join(perm)
            if pal == pal[::-1]:
                palindromes.add(pal)
    return palindromes