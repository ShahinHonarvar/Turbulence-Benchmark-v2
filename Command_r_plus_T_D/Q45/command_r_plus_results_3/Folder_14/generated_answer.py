def palindromes_between_indices(s):
    s = s.lower()
    letters_between_indices = {c for c in s[4:6] if c.isalpha()}
    palindromes = set()
    for letter in letters_between_indices:
        palindromes.add(letter * 2)
    return palindromes