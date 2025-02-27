def return_nth_smallest_ascii(s: str) -> str:
    subset = s[58:86]
    ascii_values = [ord(c) for c in subset]
    ascii_values.sort()
    return chr(ascii_values[18])