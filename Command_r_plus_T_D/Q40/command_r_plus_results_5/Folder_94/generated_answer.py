def return_n_smallest_chars(input_string: str) -> list[str]:
    smallest_87_chars = sorted(input_string, key=lambda char: ord(char), reverse=True)[:87]
    return smallest_87_chars