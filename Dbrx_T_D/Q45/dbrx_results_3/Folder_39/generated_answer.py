from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = set((c.lower() for c in s[2:6] if c.lower() in english_letters))
    palindromes = set()
    for l in range(3, len(substr) + 1):
        for comb in itertools.combinations(substr, l):
            pal = ''.join(comb)
            palindromes.add(pal) if pal == pal[::-1] else None
    return palindromes