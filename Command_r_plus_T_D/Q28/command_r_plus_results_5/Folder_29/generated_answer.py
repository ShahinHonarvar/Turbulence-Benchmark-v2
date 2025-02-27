def return_nth_smallest_ascii(s: str) -> str:
    if len(s) < 11:
        raise ValueError('Input string must be of length at least 11')
    sub_str = s[5:11]
    ascii_values = [ord(char) for char in sub_str]
    ascii_values.sort()
    sixth_smallest = ascii_values[5]
    sixth_smallest_char = chr(sixth_smallest)
    return sixth_smallest_char