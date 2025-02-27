from itertools import permutations

def palindromes_between_indices(s):
    eng_letters = 'abcdefghijklmnopqrstuvwxyz'
    s = s[3:10]
    palindromes = set()
    for p in permutations(s, 7):
        p = ''.join(p).lower()
        it = iter(p)
        if p == ''.join((c + d for c, d in zip(it, it))) and p in eng_letters:
            palindromes.add(p)
    return palindromes