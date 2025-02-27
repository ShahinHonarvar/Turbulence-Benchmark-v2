def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[34:86]
    ascii_values = [ord(c) for c in sub_s]
    ascii_values.sort()
    return chr(ascii_values[19])