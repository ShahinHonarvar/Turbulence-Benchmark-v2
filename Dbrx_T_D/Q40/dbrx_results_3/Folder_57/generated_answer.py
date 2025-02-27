def return_n_smallest_chars(input_string: str) -> list:
    sorted_chars = sorted(input_string, key=ord)
    n_smallest_chars = sorted_chars[:29]
    return n_smallest_chars[::-1]