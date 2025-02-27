def return_nth_smallest_ascii(s: str) -> str:
    sub_str = s[37:60]
    ascii_values = [ord(char) for char in sub_str]
    ascii_values.sort()
    sixth_smallest_ascii = ascii_values[5]
    sixth_smallest_char = chr(sixth_smallest_ascii)
    return sixth_smallest_char