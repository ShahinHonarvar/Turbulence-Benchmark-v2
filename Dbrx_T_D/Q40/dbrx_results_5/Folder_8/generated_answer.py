def return_n_smallest_chars(string_of_chars):
    sorted_chars = sorted(list(set(string_of_chars)))
    first_83_chars = sorted_chars[:83]
    return first_83_chars