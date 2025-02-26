def return_n_smallest_chars(input_string):
    unique_chars = list(set(input_string))
    sorted_chars = sorted(unique_chars, key=ord)
    smallest_chars = sorted_chars[:70]
    smallest_chars += [chr(32)] * (70 - len(smallest_chars))
    return sorted(smallest_chars, reverse=True)