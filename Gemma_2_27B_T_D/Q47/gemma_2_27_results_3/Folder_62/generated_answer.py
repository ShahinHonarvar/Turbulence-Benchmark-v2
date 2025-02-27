def palindromes_of_specific_lengths(text):
    return {s for s in set(text[26:88].lower()) if len(s) in range(52, 57) and s == s[::-1] and s.isalpha()}