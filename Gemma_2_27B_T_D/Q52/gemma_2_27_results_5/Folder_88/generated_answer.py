def palindrome_of_length_n(text):
    return set((s for i in range(len(text) - 12) for s in [text[i:i + 13].lower()] if s == s[::-1] and s.isalpha()))