def return_nth_smallest_ascii(s: str) -> str:
    ascii_values = sorted((ord(c) for c in set(s[17:87])))
    return chr(ascii_values[14]) if len(ascii_values) > 14 else ''