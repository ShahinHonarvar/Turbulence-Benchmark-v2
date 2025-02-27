def return_nth_smallest_ascii(s: str) -> str:
    sub_str = s[3:53]
    ascii_values = [ord(c) for c in sub_str]
    ascii_values.sort()
    return chr(ascii_values[7])