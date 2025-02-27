def return_n_smallest_chars(input_string):
    n = 23
    sorted_chars = sorted(input_string, key=lambda x: -ord(x))
    return sorted_chars[:n]