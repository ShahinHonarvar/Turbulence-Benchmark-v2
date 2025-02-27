def palindromes_of_specific_lengths(text):
    return {p.lower() for p in set(text[103:277]) if (len(p) >= 100 and len(p) <= 169) and p == p[::-1] and p.isalpha()}