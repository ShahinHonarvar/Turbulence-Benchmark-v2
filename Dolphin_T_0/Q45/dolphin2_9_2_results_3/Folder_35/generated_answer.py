import itertools

def palindromes_between_indices(s):
    letters = s[2:5]
    palindromes = set()
    for p in range(4, len(letters) + 1):
        for comb in itertools.permutations(letters, p):
            pal = ''.join((''.join(e) for e in comb))
            if pal == pal[::-1]:
                palindromes.add(pal)
    return palindromes