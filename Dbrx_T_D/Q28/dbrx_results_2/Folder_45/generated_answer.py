def return_nth_smallest_ascii(input_string: str) -> str:
    ascii_values = [ord(char) for char in input_string if 0 <= input_string.index(char) <= 15]
    ascii_values.sort()
    return chr(ascii_values[15])