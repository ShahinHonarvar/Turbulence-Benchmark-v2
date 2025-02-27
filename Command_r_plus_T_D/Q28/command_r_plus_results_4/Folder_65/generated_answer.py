def return_nth_smallest_ascii(s: str) -> str:
    ascii_chars = [chr(i) for i in range(32, 68)]
    ascii_values = [ord(c) for c in s if c in ascii_chars]
    ascii_values.sort()
    return chr(ascii_values[11]) if len(ascii_values) > 11 else ''