def return_n_smallest_chars(input_string: str) -> list:
    characters_list = sorted(set(input_string), key=ord)[::-1][:90]
    return characters_list