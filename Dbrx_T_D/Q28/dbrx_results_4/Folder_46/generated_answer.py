def return_nth_smallest_ascii(s: str) -> str:
    ascii_values = sorted((ord(c) for c in s if 34 <= s.index(c) <= 85))
    return chr(ascii_values[19]) if len(ascii_values) >= 20 else ''