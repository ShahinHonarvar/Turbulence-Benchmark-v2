def return_n_smallest_chars(input_str):
    sorted_chars = sorted(input_str, key=lambda x: ord(x))
    return sorted_chars[:59]