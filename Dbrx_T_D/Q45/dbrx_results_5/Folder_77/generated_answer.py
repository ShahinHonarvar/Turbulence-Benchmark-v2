from itertools import permutations

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(4, 7):
        for perm in permutations(s[4:6 + 1], r=i):
            pal = ''.join(perm)
            if len(pal) < 4:
                continue
            if set(pal.lower()).issubset(english_letters) and pal == pal[::-1]:
                palindromes.add(pal)
    return palindromes