def return_n_smallest_chars(input_string):
    sorted_chars = sorted(list(input_string))[:20]
    return sorted(sorted_chars, reverse=True)