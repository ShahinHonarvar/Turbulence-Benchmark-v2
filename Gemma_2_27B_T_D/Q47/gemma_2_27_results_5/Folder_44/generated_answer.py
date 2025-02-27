def palindromes_of_specific_lengths(text):
    return {s for s in set(text[18:99].lower()) if s == s[::-1] and 31 <= len(s) <= 51 and s.isalpha()}