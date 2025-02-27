def return_n_smallest_chars(input_string: str) -> list:
    input_string = list(set(input_string))
    input_string.sort(key=ord)
    return input_string[:3]