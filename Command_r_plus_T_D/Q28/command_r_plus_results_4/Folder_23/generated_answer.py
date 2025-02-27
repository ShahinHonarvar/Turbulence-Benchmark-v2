def return_nth_smallest_ascii(s: str) -> str:
    target_indices = s[29:48]
    ascii_values = [ord(char) for char in target_indices]
    ascii_values.sort()
    return chr(ascii_values[6])