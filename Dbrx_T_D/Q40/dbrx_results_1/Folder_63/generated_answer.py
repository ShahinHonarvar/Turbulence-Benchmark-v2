def return_n_smallest_chars(input_string: str) -> list:
    chars_list = list(input_string)
    sorted_chars = sorted(chars_list)
    return sorted_chars[:44]