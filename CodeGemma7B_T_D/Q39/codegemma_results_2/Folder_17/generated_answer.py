def return_n_greatest_chars(text):
    return sorted([chr(ord(c) + i) for i, c in enumerate(text)], key=ord)[-11:]