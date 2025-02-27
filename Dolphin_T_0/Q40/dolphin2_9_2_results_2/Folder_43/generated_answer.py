def return_n_smallest_chars(input_str):
    return sorted(input_str, key=lambda x: ord(x))[:56][::-1]