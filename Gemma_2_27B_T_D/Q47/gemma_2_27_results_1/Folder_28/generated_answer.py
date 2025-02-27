def palindromes_of_specific_lengths(text):
    return {s for s in set(text[32:72].lower()) if s == s[::-1] and len(s) in range(21, 33) and s.isalpha()}