def return_n_smallest_chars(input_string):
    unique_chars = list(set(input_string))
    sorted_chars = sorted(unique_chars, key=ord)
    return sorted_chars[:72] if len(sorted_chars) >= 72 else sorted_chars + [chr(0)] * (72 - len(sorted_chars))