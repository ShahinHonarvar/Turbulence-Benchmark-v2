def return_nth_smallest_ascii(s: str) -> str:
    ascii_range = [chr(i) for i in range(33, 86)]
    ascii_values = [ord(c) for c in s if c in ascii_range]
    ascii_values.sort()
    return chr(ascii_values[12]) if len(ascii_values) > 12 else ''