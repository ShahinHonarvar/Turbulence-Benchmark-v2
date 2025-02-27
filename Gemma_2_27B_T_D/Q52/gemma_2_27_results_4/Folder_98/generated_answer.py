def palindrome_of_length_n(text):
    return set((s for i in range(len(text) - 5) for s in [text[i:i + 6].lower()] if s == s[::-1] and s.isalpha()))