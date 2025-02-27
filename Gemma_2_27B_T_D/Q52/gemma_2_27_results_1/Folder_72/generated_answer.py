def palindrome_of_length_n(text):
    return {s for s in [text[i:i + 16].lower() for i in range(len(text) - 15)] if s == s[::-1] and s.isalpha()}