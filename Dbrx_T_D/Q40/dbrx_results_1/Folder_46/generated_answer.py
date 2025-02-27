def return_n_smallest_chars(input_string: str) -> list:
    input_string_list = list(input_string)
    input_string_list.sort(key=ord)
    return input_string_list[:54][::-1]