def return_n_smallest_chars(input_string: str) -> list:
    ascii_sorted_list = sorted(input_string, key=ord)
    return ascii_sorted_list[:7]