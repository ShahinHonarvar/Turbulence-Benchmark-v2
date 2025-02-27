def palindrome_of_length_n(text):
    return {t for t in [text[i:i + 23] for i in range(len(text) - 22)] if t.lower() == t.lower()[::-1]}