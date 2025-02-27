def return_n_smallest_chars(input_string):
    return sorted(sorted(input_string)[:3])[::-1]