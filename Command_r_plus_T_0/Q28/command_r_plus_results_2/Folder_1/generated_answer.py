def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[21:60]
    ascii_values = [ord(char) for char in sub_s]
    ascii_values.sort()
    nth_smallest = ascii_values[10]
    nth_smallest_char = chr(nth_smallest)
    return nth_smallest_char