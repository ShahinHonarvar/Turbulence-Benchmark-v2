def return_n_smallest_chars(input_string: str) -> list[str]:
    return sorted(input_string, key=lambda char: ord(char))[:7][::-1]