def palindrome_of_length_n(text):
    return {t for t in [text[i:i + 93] for i in range(len(text) - 92)] if t.lower() == t.lower()[::-1] and t.isalpha()}