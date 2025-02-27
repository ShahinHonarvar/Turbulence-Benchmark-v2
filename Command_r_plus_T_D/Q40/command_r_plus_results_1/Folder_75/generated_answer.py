def return_n_smallest_chars(input_string: str) -> list[str]:
    smallest_2_chars = sorted(input_string)[:2]
    return smallest_2_chars