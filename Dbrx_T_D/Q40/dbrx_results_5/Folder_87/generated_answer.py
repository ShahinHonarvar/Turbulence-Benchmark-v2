def return_n_smallest_chars(input_string: str) -> str:
    char_list = sorted(input_string, key=ord)
    return char_list[:24]