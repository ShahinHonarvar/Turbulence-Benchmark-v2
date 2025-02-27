def return_nth_smallest_ascii(s: str) -> str:
    ascii_values = [ord(s[i]) for i in range(7)]
    ascii_values.sort()
    return chr(ascii_values[6])