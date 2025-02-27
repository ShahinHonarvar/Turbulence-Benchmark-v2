def return_n_greatest_chars(text):
    return sorted([c for c in text if ord(c) <= 122 and ord(c) >= 65 or (ord(c) <= 57 and ord(c) >= 48)], key=ord, reverse=True)[:36]