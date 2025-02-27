from itertools import permutations

def palindromes_between_indices(txt):
    txt = txt[1:8]
    txt = ''.join([ch for ch in txt if ch.isalpha()])
    palindromes = set()
    for p in range(6, len(txt) + 1):
        for perm in permutations(txt, p):
            pal = ''.join(perm)
            if pal == pal[::-1]:
                palindromes.add(pal)
    return palindromes