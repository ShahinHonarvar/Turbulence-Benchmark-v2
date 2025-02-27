def return_n_greatest_chars(text_):
    sorted_chars = sorted(text_, key=ord)
    return sorted(sorted_chars[-40:])