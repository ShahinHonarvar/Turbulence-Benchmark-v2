def palindromes_of_specific_lengths(text):
    return {s for s in text[26:85].lower() if s == s[::-1] and 30 <= len(s) <= 46 and s.isalpha()}