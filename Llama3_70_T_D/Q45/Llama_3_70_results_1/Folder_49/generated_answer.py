def palindromes_between_indices(s):
    s = s[5:8].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for c in letters:
        for d in letters:
            palindromes.add(c + d + c)
    return {p for p in palindromes if len(p) >= 3}