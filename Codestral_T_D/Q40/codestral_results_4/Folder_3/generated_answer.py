def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string)
    return sorted(sorted_chars[:28], reverse=True)