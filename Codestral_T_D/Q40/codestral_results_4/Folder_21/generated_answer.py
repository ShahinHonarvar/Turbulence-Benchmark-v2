def return_n_smallest_chars(input_str):
    sorted_chars = sorted(input_str)
    n_smallest_chars = sorted_chars[:44]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars