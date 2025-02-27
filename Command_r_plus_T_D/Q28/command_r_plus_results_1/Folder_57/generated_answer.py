def return_nth_smallest_ascii(s: str) -> str:
    target_range = s[17:35]
    ascii_values = [ord(char) for char in target_range]
    ascii_values.sort()
    return chr(ascii_values[17])