def palindromes_between_indices(s):
    letters = ''.join([c for c in s[3:6] if c.isalpha()]).lower()
    palindromes = set()
    if len(letters) >= 2:
        for c in letters:
            for p in [''.join([c, x, c]) for x in letters]:
                palindromes.add(p)
    return palindromes