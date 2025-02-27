def return_n_greatest_chars(text):
    n = 20
    return sorted(sorted(text), key=ord, reverse=True)[:n]