def return_nth_smallest_ascii(s: str) -> str:
    subset = s[9:23]
    ascii_values = [ord(c) for c in subset]
    ascii_values.sort()
    fourth_smallest = ascii_values[3]
    return chr(fourth_smallest)