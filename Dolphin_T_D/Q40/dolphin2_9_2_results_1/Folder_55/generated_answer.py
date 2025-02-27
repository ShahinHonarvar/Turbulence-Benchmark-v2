def return_n_smallest_chars(input_str):
    n = 75
    chars = list(input_str)
    chars.sort()
    return chars[::-1][:n]