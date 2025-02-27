def return_nth_smallest_ascii(s: str) -> str:
    subset = s[12:56]
    ascii_values = [ord(char) for char in subset]
    ascii_values.sort()
    return chr(ascii_values[16])