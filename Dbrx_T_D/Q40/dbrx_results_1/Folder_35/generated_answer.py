def return_n_smallest_chars(input_string: str) -> list:
    chars_list = list(input_string)
    chars_list.sort(key=ord)
    return chars_list[:7]