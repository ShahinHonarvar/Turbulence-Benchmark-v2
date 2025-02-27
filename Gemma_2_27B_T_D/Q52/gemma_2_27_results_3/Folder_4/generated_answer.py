def palindrome_of_length_n(text):
    return {t for t in [text[i:i + 15].lower() for i in range(len(text) - 14)] if t == t[::-1] and t.isalpha()}