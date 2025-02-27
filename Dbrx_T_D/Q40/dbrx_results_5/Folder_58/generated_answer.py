def return_n_smallest_chars(input_string: str) -> list:
    chars = sorted(list(input_string))
    chars = chars[::-1]
    return chars[:49]