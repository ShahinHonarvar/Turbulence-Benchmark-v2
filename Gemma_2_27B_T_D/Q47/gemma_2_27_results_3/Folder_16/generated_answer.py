def palindromes_of_specific_lengths(text):
    return {s for s in set(text[15:87].lower()) if s == s[::-1] and len(s) in range(51, 61) and s.isalpha()}