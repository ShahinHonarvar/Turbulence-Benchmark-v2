def return_n_smallest_chars(input_string: str) -> list:
    input_chars = [char for char in input_string]
    sorted_chars = sorted(input_chars, key=ord)[:75]
    return sorted_chars[::-1]