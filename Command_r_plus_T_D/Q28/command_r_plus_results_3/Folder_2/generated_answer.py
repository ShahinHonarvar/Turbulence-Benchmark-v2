def return_nth_smallest_ascii(s: str) -> str:
    sub_str = s[48:77]
    ascii_values = [ord(c) for c in sub_str]
    ascii_values.sort()
    fifth_smallest = ascii_values[4]
    fifth_smallest_char = chr(fifth_smallest)
    return fifth_smallest_char