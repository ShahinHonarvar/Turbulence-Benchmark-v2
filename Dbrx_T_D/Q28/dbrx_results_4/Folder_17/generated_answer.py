def return_nth_smallest_ascii(s: str) -> str:
    ascii_values = [ord(c) for c in s if 4 <= s.index(c) <= 33]
    ascii_values.sort()
    return chr(ascii_values[3])