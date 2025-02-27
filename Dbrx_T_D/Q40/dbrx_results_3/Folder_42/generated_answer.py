def return_n_smallest_chars(input_string: str) -> list:
    ascii_sorted_list = sorted(input_string, key=ord)
    n_smallest_chars = ascii_sorted_list[:59]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars