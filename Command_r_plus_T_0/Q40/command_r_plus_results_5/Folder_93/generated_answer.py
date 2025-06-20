def return_n_smallest_chars(input_string: str) -> list[str]:
    sorted_string = sorted(input_string, key=lambda char: ord(char), reverse=True)
    return sorted_string[:77]