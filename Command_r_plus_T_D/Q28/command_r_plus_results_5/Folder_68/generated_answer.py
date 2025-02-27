def return_nth_smallest_ascii(s: str) -> str:
    if not s:
        raise ValueError('Input string is empty.')
    if len(s) < 11:
        raise ValueError('Input string length is less than 11.')
    sub_s = s[:11]
    ascii_values = [ord(char) for char in sub_s]
    ascii_values.sort()
    return chr(ascii_values[10])