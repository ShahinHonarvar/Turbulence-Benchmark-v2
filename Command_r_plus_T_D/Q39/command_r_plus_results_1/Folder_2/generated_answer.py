def return_n_greatest_chars(input_string: str) -> list[str]:
    input_string = input_string.strip()
    if len(input_string) < 48:
        raise ValueError('Input string must contain at least 48 characters.')
    ascii_list = [(ord(char), char) for char in input_string]
    ascii_list.sort(key=lambda x: x[0], reverse=True)
    return [char for _, char in ascii_list[:48]]