def return_n_smallest_chars(input_string):
    unique_chars = set(input_string)
    sorted_chars = sorted(unique_chars, key=ord)
    smallest_chars = sorted_chars[:44]
    result = sorted(smallest_chars, reverse=True)
    return result