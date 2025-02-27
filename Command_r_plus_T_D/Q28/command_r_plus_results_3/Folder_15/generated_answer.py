def return_nth_smallest_ascii(s: str) -> str:
    s_slice = s[:6]
    ascii_values = [ord(c) for c in s_slice]
    ascii_values.sort()
    return chr(ascii_values[5])