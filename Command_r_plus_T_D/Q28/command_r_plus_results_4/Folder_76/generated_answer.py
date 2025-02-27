def return_nth_smallest_ascii(s: str) -> str:
    if not s:
        raise ValueError('Input string is empty.')
    if len(s) < 67:
        raise ValueError('Input string length is less than 67.')
    ascii_values = [ord(s[i]) for i in range(18, 67)]
    ascii_values.sort()
    return chr(ascii_values[18])