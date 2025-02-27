def return_nth_smallest_ascii(s: str) -> str:
    if len(s) < 19:
        raise ValueError('Input string must have at least 19 characters.')
    ascii_values = [ord(char) for char in s[:19]]
    ascii_values.sort()
    return chr(ascii_values[12])