def return_n_smallest_chars(input_string: str) -> list[str]:
    sorted_string = sorted(input_string, key=lambda char: ord(char))
    smallest_chars = sorted_string[:38]
    return smallest_chars[::-1]