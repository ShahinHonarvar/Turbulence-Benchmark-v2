def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[60:89]
    ascii_values = [ord(char) for char in sub_s]
    ascii_values.sort()
    seventh_smallest = ascii_values[6]
    seventh_smallest_char = chr(seventh_smallest)
    return seventh_smallest_char