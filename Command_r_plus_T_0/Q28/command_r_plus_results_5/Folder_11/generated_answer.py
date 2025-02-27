def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[9:60]
    ascii_values = [ord(char) for char in sub_s]
    ascii_values.sort()
    sixth_smallest = ascii_values[5]
    sixth_smallest_char = chr(sixth_smallest)
    return sixth_smallest_char