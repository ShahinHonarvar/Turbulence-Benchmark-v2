def return_n_greatest_chars(text):
    return sorted(list(text), key=lambda x: -ord(x))[:43]