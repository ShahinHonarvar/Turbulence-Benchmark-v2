def return_n_smallest_chars(input_string: str) -> str:
    sorted_chars = sorted(list(input_string))
    return ''.join(sorted_chars[:35])