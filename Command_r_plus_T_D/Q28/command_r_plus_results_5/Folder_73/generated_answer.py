def return_nth_smallest_ascii(s: str) -> str:
    if not s:
        raise ValueError('Input string is empty.')
    if len(s) < 70:
        raise ValueError('Input string must have at least 70 characters.')
    ascii_values = [ord(s[i]) for i in range(70)]
    ascii_values.sort()
    return chr(ascii_values[9])