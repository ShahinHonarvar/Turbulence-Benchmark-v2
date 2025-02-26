def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string)[:90]
    return sorted(sorted_chars, reverse=True)