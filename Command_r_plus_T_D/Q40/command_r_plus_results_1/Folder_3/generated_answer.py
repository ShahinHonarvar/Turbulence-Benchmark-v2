def return_n_smallest_chars(input_string: str) -> list[str]:
    sorted_chars = sorted(input_string, key=lambda char: ord(char))[:28]
    return sorted_chars[::-1]