def return_n_smallest_chars(input_string: str) -> list:
    ascii_values = sorted((ord(c) for c in input_string))
    smallest_chars = [chr(value) for value in ascii_values[:85]]
    smallest_chars.sort(reverse=True)
    return smallest_chars