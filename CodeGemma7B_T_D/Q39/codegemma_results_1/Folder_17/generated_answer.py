def return_n_greatest_chars(chars):
    ordered_chars = sorted(chars, key=ord)
    return ordered_chars[-11:]