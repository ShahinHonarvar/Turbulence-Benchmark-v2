def return_n_greatest_chars(text):
    sorted_chars = sorted(text, key=ord)
    return sorted_chars[-45:]