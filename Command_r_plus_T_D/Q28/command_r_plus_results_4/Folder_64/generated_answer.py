def return_nth_smallest_ascii(s: str) -> str:
    if len(s) < 7:
        raise ValueError('Input string must have at least 7 characters.')
    ascii_values = [ord(s[i]) for i in range(7)]
    ascii_values.sort()
    return chr(ascii_values[6])