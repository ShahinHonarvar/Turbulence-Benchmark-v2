def return_n_smallest_chars(input_string: str) -> list:
    sorted_list = sorted(list(input_string))
    return sorted_list[:21]