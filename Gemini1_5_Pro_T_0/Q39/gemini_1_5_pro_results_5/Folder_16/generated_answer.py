def return_n_greatest_chars(text):
    return sorted([c for c in text if ord(c) >= 32], key=ord, reverse=True)[:64]