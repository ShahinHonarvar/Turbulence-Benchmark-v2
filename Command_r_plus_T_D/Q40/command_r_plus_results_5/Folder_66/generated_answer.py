def return_n_smallest_chars(input_string: str) -> list[str]:
    smallest_chars = sorted(input_string, key=lambda x: ord(x))[:33]
    return smallest_chars[::-1]