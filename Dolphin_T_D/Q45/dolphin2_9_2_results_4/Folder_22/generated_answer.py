def palindromes_between_indices(s):
    letters = [c for c in s[5:7] if c.isalpha() and c.isascii()]
    palindromes = set()
    for letter in letters:
        palindromes.add(letter.lower())
        palindromes.update([p + letter.lower() + p for p in palindromes if len(p) < 2])
    return palindromes