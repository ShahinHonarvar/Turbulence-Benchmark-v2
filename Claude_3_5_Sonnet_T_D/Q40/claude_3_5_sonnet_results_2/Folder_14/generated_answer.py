def return_n_smallest_chars(input_string):
    unique_chars = list(set(input_string))
    sorted_chars = sorted(unique_chars, key=ord)
    return sorted_chars[:69] if len(sorted_chars) >= 69 else sorted_chars + [chr(0)] * (69 - len(sorted_chars))