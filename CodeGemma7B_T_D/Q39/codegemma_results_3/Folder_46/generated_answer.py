def return_n_greatest_chars(text):
    return sorted(list(text), key=ord, reverse=True)[:54]