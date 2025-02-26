def return_n_smallest_chars(input_string):
    unique_chars = list(set(input_string))
    sorted_chars = sorted(unique_chars, key=ord)
    smallest_35 = sorted_chars[:35]
    return sorted(smallest_35, reverse=True)