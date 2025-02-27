def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string, key=lambda x: ord(x))
    return sorted(sorted_chars[:6], key=lambda x: -ord(x))