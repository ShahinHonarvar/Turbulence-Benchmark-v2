def return_nth_smallest_ascii(s: str) -> str:
    ascii_range = [chr(i) for i in range(32, 68)]
    ascii_values = [ord(c) for c in s if c in ascii_range]
    ascii_values.sort()
    return chr(ascii_values[11])