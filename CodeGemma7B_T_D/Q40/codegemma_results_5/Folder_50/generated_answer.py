def return_n_smallest_chars(input_str):
    return sorted(input_str, key=ord, reverse=True)[:16]