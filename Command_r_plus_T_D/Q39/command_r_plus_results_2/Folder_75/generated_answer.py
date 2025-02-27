def return_n_greatest_chars(input_string: str) -> list[str]:
    if len(input_string) < 2:
        raise ValueError('Input string must contain at least 2 characters.')
    char_list = list(input_string)
    char_list.sort(key=lambda x: ord(x), reverse=True)
    return char_list[:2]