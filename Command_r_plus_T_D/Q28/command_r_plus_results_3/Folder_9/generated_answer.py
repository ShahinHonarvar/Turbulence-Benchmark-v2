def return_nth_smallest_ascii(s: str) -> str:
    sub_str = s[10:91]
    ascii_values = [ord(char) for char in sub_str]
    ascii_values.sort()
    return chr(ascii_values[19])