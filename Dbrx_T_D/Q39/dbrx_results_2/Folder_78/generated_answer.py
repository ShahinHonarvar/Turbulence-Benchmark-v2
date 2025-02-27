def return_n_greatest_chars(input_string: str) -> list:
    input_string = ''.join(sorted(set(input_string), key=ord))
    return sorted(input_string, key=ord, reverse=True)[:43]