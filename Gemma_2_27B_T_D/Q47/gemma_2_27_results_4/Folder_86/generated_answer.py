def palindromes_of_specific_lengths(text):
    return {p for p in set(text[30:96].lower()) if len(p) in range(34, 56) and p == p[::-1] and all((c.isalpha() for c in p))}