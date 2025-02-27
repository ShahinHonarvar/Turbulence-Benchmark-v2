def return_n_greatest_chars(input_string: str) -> list[str]:
    input_string_sorted = sorted(input_string, reverse=True)
    return input_string_sorted[:36]