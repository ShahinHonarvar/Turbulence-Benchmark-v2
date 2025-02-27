def return_nth_smallest_ascii(s: str) -> str:
    sub_str = s[28:55]
    ascii_values = [ord(char) for char in sub_str]
    ascii_values.sort()
    nth_smallest = ascii_values[13]
    return chr(nth_smallest)