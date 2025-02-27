def palindrome_of_length_n(text):
    return {t for t in [text[i:i + 59] for i in range(len(text) - 58)] if t.lower() == t.lower()[::-1] and t.isalpha()}