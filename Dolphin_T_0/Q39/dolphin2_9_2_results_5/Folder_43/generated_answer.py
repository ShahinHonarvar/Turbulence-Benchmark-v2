def return_n_greatest_chars(input_str):
    chars = sorted(input_str, key=lambda c: -ord(c))
    return chars[:56]