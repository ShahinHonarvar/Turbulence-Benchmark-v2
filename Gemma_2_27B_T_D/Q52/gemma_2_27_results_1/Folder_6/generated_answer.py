def palindrome_of_length_n(text):
    return {t for t in [text[i:i + 474] for i in range(len(text) - 473)] if t.lower() == t[::-1].lower() and t.isalpha()}