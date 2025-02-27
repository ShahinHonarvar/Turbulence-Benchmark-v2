def return_nth_smallest_ascii(s: str) -> str:
    ascii_values = sorted((ord(c) for c in set(s[25:89])))
    return chr(ascii_values[10]) if len(ascii_values) > 10 else ''