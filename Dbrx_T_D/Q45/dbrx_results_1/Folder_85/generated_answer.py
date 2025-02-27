def palindromes_between_indices(s):
    s = s[2:9].lower()
    letters = {c for c in s if c.isalpha()}
    palindromes = {p for p in letters if s.count(s.count(p) * p) >= 7}
    return palindromes