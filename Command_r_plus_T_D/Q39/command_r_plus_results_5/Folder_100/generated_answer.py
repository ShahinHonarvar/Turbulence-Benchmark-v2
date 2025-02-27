def return_n_greatest_chars(input_string: str) -> list[str]:
    sorted_chars = sorted(input_string, key=lambda char: ord(char), reverse=True)
    return sorted_chars[:72]