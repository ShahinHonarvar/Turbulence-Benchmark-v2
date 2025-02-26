def return_n_smallest_chars(input_string):
    sorted_chars = sorted(set(input_string))
    smallest_54 = sorted_chars[:54]
    return sorted(smallest_54, reverse=True)