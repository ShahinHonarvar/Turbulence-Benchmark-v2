def palindromes_of_specific_lengths(text):
    return {p for p in set(text[12:93].lower()) if p == p[::-1] and len(p) in range(42, 78) and p.isalpha()}