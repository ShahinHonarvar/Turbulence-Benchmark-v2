from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:5].lower()
    letters = list(set(s) - set('0123456789'))
    if len(letters) < 2:
        return set()
    palindromes = set()
    for perm in permutations(letters):
        pal = ''.join(perm)
        if len(pal) < 4:
            continue
        if pal == pal[::-1]:
            palindromes.add(pal)
    return palindromes