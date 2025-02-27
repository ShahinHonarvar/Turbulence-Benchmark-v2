def return_n_smallest_chars(input_string: str) -> list[str]:
    smallest_chars = sorted(input_string)[:5]
    return smallest_chars