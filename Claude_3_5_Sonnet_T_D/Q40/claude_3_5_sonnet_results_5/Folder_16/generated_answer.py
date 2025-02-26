def return_n_smallest_chars(input_string):
    unique_chars = list(set(input_string))
    sorted_chars = sorted(unique_chars)
    smallest_64 = sorted_chars[:64]
    return sorted(smallest_64, reverse=True)