def return_n_smallest_chars(input_string: str) -> list[str]:
    input_string_sorted = sorted(input_string)
    smallest_chars = input_string_sorted[:90]
    return smallest_chars