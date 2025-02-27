def return_n_smallest_chars(input_string: str) -> list[str]:
    smallest_24_chars = sorted(input_string, key=lambda char: ord(char))[:24]
    return smallest_24_chars[::-1]