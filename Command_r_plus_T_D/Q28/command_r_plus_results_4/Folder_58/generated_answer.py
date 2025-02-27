def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[8:27]
    ascii_values = [ord(c) for c in sub_s]
    ascii_values.sort()
    sixth_smallest = ascii_values[5]
    return chr(sixth_smallest)