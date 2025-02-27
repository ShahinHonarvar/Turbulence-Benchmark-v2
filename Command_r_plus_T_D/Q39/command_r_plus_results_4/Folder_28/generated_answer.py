def return_n_greatest_chars(input_string: str) -> list[str]:
    input_string_sorted = sorted(input_string, key=lambda char: ord(char), reverse=True)
    return input_string_sorted[:3]