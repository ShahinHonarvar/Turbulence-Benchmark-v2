def return_n_greatest_chars(text):
    return sorted([c for c in text if ord(c) > 32 and ord(c) < 127], key=ord, reverse=True)[:79]