def return_n_smallest_chars(input_string: str) -> list[str]:
    ascii_sorted_chars = sorted(input_string, key=ord)
    return ascii_sorted_chars[:72][::-1]