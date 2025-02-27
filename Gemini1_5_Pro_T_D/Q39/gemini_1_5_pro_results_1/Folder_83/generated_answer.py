def return_n_greatest_chars(text):
    return sorted([c for c in text if ord(c) >= 32], reverse=True)[:38]