def return_n_smallest_chars(input_string):
    sorted_chars = sorted(set(input_string))
    result = sorted_chars[:65]
    return sorted(result, reverse=True)