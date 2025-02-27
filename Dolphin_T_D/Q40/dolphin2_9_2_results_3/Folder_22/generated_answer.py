def return_n_smallest_chars(input_str):
    chars = list(input_str)
    chars.sort()
    return chars[:76]