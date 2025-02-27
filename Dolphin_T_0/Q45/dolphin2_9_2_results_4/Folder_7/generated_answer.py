from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = {}
    for i in range(1, 10):
        for j in range(i + 2, len(s) + 1):
            substr = s[i:j]
            if len(substr) != len(set(substr)):
                continue
            for p in permutations(substr.lower()):
                pal = ''.join(p)
                if pal == pal[::-1]:
                    palindromes.add(pal)
    return palindromes