def palindrome_of_length_at_least_n(text):
    return {t for t in set(text.lower()) if len(t) >= 76 and t == t[::-1] and all((c.isalpha() for c in t))}