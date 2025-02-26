def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string)
    smallest_chars = sorted_chars[:52] if len(sorted_chars) >= 52 else sorted_chars
    return sorted(smallest_chars, reverse=True)