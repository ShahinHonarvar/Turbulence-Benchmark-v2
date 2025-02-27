def return_n_smallest_chars(input_string: str) -> list:
    ascii_list = sorted(list(input_string), key=ord)[:84]
    return ascii_list[::-1]