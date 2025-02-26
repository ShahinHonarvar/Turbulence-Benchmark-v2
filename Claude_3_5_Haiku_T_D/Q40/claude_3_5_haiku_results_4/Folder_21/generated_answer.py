def return_n_smallest_chars(input_string):
    sorted_chars = sorted(set(input_string))[:44]
    return sorted(sorted_chars, reverse=True)