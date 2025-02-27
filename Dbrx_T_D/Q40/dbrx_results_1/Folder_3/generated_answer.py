def return_n_smallest_chars(input_string: str) -> list:
    char_list = list(set(input_string))
    char_list.sort(key=lambda x: ord(x))
    return char_list[:28][::-1]