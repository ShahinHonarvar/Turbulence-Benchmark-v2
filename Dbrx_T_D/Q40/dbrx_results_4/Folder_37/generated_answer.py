def return_n_smallest_chars(input_string: str) -> list:
    ascii_values = [ord(char) for char in input_string]
    sorted_ascii_values = sorted(ascii_values)[:26]
    sorted_characters = [chr(value) for value in sorted_ascii_values]
    return sorted_characters[::-1]