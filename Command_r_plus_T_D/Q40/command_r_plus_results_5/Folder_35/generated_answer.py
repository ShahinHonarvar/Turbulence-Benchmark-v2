def return_n_smallest_chars(input_string: str) -> list[str]:
    smallest_chars = sorted(input_string)[:7]
    return smallest_chars