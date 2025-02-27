def return_nth_smallest_ascii(s: str) -> str:
    subset = s[8:66]
    ascii_values = [ord(c) for c in subset]
    ascii_values.sort()
    sixth_smallest = ascii_values[5]
    sixth_smallest_char = chr(sixth_smallest)
    return sixth_smallest_char