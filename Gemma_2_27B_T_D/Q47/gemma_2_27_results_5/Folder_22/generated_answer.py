def palindromes_of_specific_lengths(text):
    return {s for s in set(text[100:201].lower().split()) if len(s) in range(5, 11) and s == s[::-1] and s.isalpha()}