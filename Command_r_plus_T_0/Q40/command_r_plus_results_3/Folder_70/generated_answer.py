def return_n_smallest_chars(input_string: str) -> list[str]:
    char_list = list(input_string)
    char_list.sort()
    return char_list[:2]