def return_nth_smallest_ascii(s: str) -> str:
    if len(s) < 12:
        raise ValueError('Input string must have at least 12 characters.')
    sub_s = s[:12]
    ascii_values = [ord(char) for char in sub_s]
    ascii_values.sort()
    return chr(ascii_values[11])