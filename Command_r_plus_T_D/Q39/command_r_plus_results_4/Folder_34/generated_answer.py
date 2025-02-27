def return_n_greatest_chars(input_string: str) -> list[str]:
    if len(input_string) < 9:
        raise ValueError('Input string must contain at least 9 characters.')
    sorted_chars = sorted(input_string, key=lambda char: ord(char), reverse=True)
    return sorted_chars[:9]