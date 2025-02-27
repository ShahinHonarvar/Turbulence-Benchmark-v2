def palindromes_between_indices(string):
    letters = ''.join(sorted([c for c in string[4:9] if c.isalpha()]))
    palindromes = set()
    for length in range(6, len(letters) + 1):
        palindromes |= set(map(''.join, combinations(letters, length)))
    return {pal for pal in palindromes if pal == pal.lower() and pal == pal[::-1]}