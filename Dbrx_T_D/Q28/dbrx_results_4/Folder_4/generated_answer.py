def return_nth_smallest_ascii(input_str: str) -> str:
    ascii_values = [ord(char) for char in input_str if 9 <= input_str.index(char) <= 22]
    ascii_values.sort()
    return chr(ascii_values[3])