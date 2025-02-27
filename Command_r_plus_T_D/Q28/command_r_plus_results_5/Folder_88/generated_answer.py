def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[38:65]
    ascii_values = [ord(char) for char in sub_s]
    ascii_values.sort()
    nth_smallest_ascii = ascii_values[13]
    nth_smallest_char = chr(nth_smallest_ascii)
    return nth_smallest_char