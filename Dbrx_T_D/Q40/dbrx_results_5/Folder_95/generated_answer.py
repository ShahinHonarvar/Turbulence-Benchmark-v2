def return_n_smallest_chars(input_string: str) -> str:
    sorted_chars = sorted(list(set(input_string)), key=ord)
    return ''.join(sorted_chars[:36])