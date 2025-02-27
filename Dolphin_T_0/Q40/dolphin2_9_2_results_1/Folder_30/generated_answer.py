def return_n_smallest_chars(input_str):
    chars = list(input_str)
    chars.sort()
    chars = chars[:72]
    return chars