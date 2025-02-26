def return_n_smallest_chars(input_string):
    sorted_chars = sorted(set(input_string))
    return sorted(sorted_chars[:49], reverse=True)