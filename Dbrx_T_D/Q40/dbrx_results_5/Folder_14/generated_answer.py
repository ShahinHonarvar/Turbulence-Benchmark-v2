def return_n_smallest_chars(input_str: str) -> list:
    chars_list = list(input_str)
    chars_list.sort(key=lambda x: ord(x))
    return chars_list[:69]