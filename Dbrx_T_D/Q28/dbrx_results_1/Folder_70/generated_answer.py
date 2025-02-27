def return_nth_smallest_ascii(s: str) -> str:
    ascii_values = sorted((ord(c) for c in s[28:55]))
    return chr(ascii_values[13])