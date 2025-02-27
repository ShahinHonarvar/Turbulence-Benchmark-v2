def return_n_smallest_chars(input_string: str) -> list[str]:
    input_string = sorted(input_string)
    return [input_string[0], input_string[1]]