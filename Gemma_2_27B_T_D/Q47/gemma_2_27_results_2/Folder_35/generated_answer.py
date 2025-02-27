def palindromes_of_specific_lengths(s):
    return {p for p in set(s[34:91].lower()) if p == p[::-1] and 14 <= len(p) <= 39 and p.isalpha()}