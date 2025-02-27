def palindrome_of_length_at_least_n(text):
    return {p for p in set(''.join((c for c in text if c.isalpha())).lower().split()) if len(p) >= 48 and p == p[::-1]}