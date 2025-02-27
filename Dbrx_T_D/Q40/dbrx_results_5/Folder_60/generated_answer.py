def return_n_smallest_chars(input_string: str) -> list:
    char_list = sorted(list(set(input_string)))[:28]
    return char_list