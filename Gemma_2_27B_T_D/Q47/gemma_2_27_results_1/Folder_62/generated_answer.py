def palindromes_of_specific_lengths(text):
    return {p for p in set(text[26:88].lower()) if len(p) in range(52, 57) and p == p[::-1] and p.isalpha()}