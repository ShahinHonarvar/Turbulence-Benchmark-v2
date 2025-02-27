from collections import Counter
    import itertools

def palindromes_between_indices(s):
    s = s[4:9].lower()
    counter = Counter((c for c in s if c.isalpha()))
    letters = ''.join((c * n for c, n in counter.items()))
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for combo in itertools.permutations(letters, r):
            combo = ''.join(combo)
            if combo == combo[::-1]:
                palindromes.add(combo)
    return palindromes