def return_n_greatest_chars(input_string: str) -> list[str]:
    if not isinstance(input_string, str):
        raise ValueError('Input must be a string.')
    if len(input_string) < 2:
        raise ValueError('Input string must contain at least 2 characters.')
    char_list = list(input_string)
    char_list.sort(key=lambda x: ord(x), reverse=True)
    return char_list[:2]