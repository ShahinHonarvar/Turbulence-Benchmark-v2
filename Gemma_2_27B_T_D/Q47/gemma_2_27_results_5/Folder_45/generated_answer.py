def palindromes_of_specific_lengths(text):
    return {p.lower() for p in set(text[70:141]) if len(p) in range(3, 61) and p.lower() == p.lower()[::-1] and p.isalpha()}