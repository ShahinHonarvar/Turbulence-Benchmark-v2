def return_n_smallest_chars(input_string: str) -> list[str]:
    smallest_82_chars = sorted(input_string, key=lambda char: ord(char), reverse=True)[:82]
    return smallest_82_chars