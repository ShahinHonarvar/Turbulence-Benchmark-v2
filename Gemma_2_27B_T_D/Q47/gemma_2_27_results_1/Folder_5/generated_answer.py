def palindromes_of_specific_lengths(text):
    return {p for p in set(text[63:71].lower()) if len(p) in [4, 5] and p == p[::-1] and p.isalpha()}