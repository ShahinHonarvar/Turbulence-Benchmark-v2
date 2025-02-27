def return_n_smallest_chars(input_string: str) -> list:
    input_string = sorted(input_string, key=ord)
    return input_string[:37][::-1]