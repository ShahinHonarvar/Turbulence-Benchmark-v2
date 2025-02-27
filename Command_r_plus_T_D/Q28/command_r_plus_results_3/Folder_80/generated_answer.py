def return_nth_smallest_ascii(s: str) -> str:
    target_slice = s[51:90]
    ascii_values = [ord(char) for char in target_slice]
    ascii_values.sort()
    return chr(ascii_values[13])