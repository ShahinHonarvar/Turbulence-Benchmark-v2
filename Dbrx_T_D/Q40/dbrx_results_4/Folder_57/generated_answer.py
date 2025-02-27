def return_n_smallest_chars(input_string):
    sorted_chars = sorted(set(input_string), key=ord)
    n_chars = sorted_chars[:29]
    n_chars.reverse()
    return n_chars