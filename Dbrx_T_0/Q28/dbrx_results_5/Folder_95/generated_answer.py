def return_nth_smallest_ascii(s: str) -> str:
    ascii_values = sorted((ord(c) for c in s if 1 <= s.index(c) <= 46))
    return chr(ascii_values[12])