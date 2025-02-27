def return_n_greatest_chars(text):
    sorted_chars = sorted(text)
    greatest_chars = sorted_chars[-52:]
    return greatest_chars