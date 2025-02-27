def return_nth_smallest_ascii(s: str) -> str:
    sub_str = s[29:34]
    ascii_values = [ord(char) for char in sub_str]
    ascii_values.sort()
    fifth_smallest = ascii_values[4]
    fifth_smallest_char = chr(fifth_smallest)
    return fifth_smallest_char