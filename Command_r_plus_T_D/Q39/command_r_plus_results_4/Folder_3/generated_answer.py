def return_n_greatest_chars(input_string: str) -> list[str]:
    input_string = input_string.strip()
    if len(input_string) < 28:
        raise ValueError('Input string must contain at least 28 characters.')
    char_list = list(input_string)
    char_list.sort(key=lambda x: ord(x), reverse=True)
    return char_list[:28]