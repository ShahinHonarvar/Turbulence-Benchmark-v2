def palindrome_of_length_at_least_n(text):
    return {s for s in text.lower() if s == s[::-1] and len(s) >= 63 and s.isalpha()}