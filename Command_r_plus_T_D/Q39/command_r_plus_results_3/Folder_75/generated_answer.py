def return_n_greatest_chars(input_string: str) -> list[str]:
    if len(input_string) < 2:
        raise ValueError('Input string must contain at least 2 characters.')
    sorted_string = sorted(input_string, key=lambda x: ord(x), reverse=True)
    return sorted_string[:2]