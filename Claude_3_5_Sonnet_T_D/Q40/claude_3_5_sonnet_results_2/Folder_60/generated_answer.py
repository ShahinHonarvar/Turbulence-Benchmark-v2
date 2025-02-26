def return_n_smallest_chars(input_string):
    unique_chars = set(input_string)
    sorted_chars = sorted(unique_chars, key=lambda x: ord(x))
    return sorted_chars[:28]