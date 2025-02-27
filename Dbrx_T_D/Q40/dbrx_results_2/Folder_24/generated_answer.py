def return_n_smallest_chars(input_string: str) -> list:
    return sorted(input_string, key=ord)[::-1][:32]