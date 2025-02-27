def return_n_smallest_chars(input_string: str) -> list:
    return sorted(list(set(input_string)))[-48:]