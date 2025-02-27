def palindrome_of_length_n(text):
    return {t for t in [text[i:i + 90] for i in range(len(text) - 89)] if t.lower() == t.lower()[::-1] and all((c.isalpha() for c in t))}