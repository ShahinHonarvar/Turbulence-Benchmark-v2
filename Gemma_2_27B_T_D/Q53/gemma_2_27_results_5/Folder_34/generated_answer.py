def palindrome_of_length_at_least_n(text):
    return {t for t in set(''.join((c for c in text if c.isalpha())).lower().split()) if len(t) >= 68 and t == t[::-1]}