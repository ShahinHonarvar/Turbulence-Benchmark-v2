def return_n_greatest_chars(text):
    return sorted([c for c in text if c.isalnum()], key=ord, reverse=True)[:65]