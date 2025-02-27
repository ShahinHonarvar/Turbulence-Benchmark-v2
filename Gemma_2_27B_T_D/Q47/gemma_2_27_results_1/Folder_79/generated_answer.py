def palindromes_of_specific_lengths(text):
    return {p for p in set(text[1:9].lower()) if p == p[::-1] and 3 <= len(p) <= 4 and p.isalpha()}