def return_nth_smallest_ascii(s: str) -> str:
    ascii_values = [ord(c) for c in s[:46]]
    ascii_values.sort()
    return chr(ascii_values[9])