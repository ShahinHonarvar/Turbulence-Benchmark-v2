def return_n_greatest_chars(input_string: str) -> list[str]:
    return sorted(input_string, key=lambda char: ord(char), reverse=True)[:90]