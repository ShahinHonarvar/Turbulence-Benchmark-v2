def return_n_smallest_chars(input_string):
    sorted_chars = sorted(set(input_string))[:11]
    return sorted(sorted_chars, reverse=True)