def palindromes_between_indices(s):
    s = s[3:9].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for c in letters:
        for p in set((''.join(p) for r in range(1, 4) for p in itertools.product(letters, repeat=r) if len(p) >= 5 and p == p[::-1] and (c in p))):
            palindromes.add(p)
    return palindromes