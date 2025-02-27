def return_n_smallest_chars(input_string: str) -> list:
    char_list = sorted(list(set(input_string)))
    return char_list[-84:][::-1]