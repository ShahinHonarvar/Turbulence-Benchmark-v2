def palindromes_of_specific_lengths(text):
    return {s for s in set(text[34:91].lower()) if s == s[::-1] and len(s) in range(14, 40) and s.isalpha()}