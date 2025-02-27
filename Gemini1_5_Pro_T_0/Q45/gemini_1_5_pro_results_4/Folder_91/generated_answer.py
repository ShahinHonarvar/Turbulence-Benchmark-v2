from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:7].lower()
    letters = set(s) & set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for p in permutations(letters, i):
            if p == tuple(reversed(p)):
                palindromes.add(''.join(p))
    return palindromes