def return_n_smallest_chars(input_string: str) -> list[str]:
    input_string_list = list(input_string)
    input_string_list.sort()
    return input_string_list[:3]