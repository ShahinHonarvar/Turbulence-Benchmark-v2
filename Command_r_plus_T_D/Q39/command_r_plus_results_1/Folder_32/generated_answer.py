def return_n_greatest_chars(input_string: str) -> list[str]:
    input_string = sorted(input_string, key=lambda x: ord(x), reverse=True)
    return input_string[:8]