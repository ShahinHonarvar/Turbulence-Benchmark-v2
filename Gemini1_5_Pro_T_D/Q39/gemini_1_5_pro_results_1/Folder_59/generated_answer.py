def return_n_greatest_chars(text_):
    sorted_chars = sorted(text_, key=ord, reverse=True)
    return sorted_chars[:13]