def return_n_smallest_chars(str):
    ascii_values = sorted([ord(char) for char in str])
    return [chr(value) for value in ascii_values[:29]]