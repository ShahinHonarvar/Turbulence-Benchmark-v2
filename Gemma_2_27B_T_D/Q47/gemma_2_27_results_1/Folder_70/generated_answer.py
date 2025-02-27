def palindromes_of_specific_lengths(text):
    return {p for p in set(text[10:71].lower()) if len(p) in range(24, 53) and p == p[::-1] and p.isalpha()}