def palindromes_between_indices(s):
    s = s[:3].lower()
    letters = sorted(set((c for c in s if c.isalpha())))
    palindromes = set()
    for a in letters:
        for b in letters:
            if a != b:
                palindromes.add(a + b + a)
    return palindromes