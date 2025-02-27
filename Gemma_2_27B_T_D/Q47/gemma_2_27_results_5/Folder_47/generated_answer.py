def palindromes_of_specific_lengths(text):
    return {s for s in set(text[39:95].lower().split()) if len(s) in range(14, 53) and s == s[::-1] and s.isalpha()}