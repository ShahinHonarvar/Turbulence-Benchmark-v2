def return_n_greatest_chars(text):
    unique_chars = sorted(set(text), key=ord, reverse=True)
    return unique_chars[:36]