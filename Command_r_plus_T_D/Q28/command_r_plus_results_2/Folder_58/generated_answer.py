def return_nth_smallest_ascii(s: str) -> str:
    sub_str = s[8:27]
    ascii_values = [ord(char) for char in sub_str]
    ascii_values.sort()
    sixth_smallest = ascii_values[5]
    return chr(sixth_smallest)