def return_nth_smallest_ascii(s: str) -> str:
    if len(s) < 18:
        raise ValueError('Input string must be at least 18 characters long.')
    sub_s = s[:18]
    ascii_values = [ord(char) for char in sub_s]
    ascii_values.sort()
    return chr(ascii_values[17])