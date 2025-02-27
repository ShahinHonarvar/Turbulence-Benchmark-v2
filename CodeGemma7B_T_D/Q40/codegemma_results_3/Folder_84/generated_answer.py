def return_n_smallest_chars(given_string):
    unique_chars = set(given_string)
    ascii_values = sorted([ord(char) for char in unique_chars])
    return [chr(value) for value in ascii_values[:10]]