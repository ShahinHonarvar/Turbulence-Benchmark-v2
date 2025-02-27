def return_n_greatest_chars(text):
    return sorted(text, key=ord, reverse=True)[:6]