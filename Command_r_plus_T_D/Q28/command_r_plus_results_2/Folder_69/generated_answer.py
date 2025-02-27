def return_nth_smallest_ascii(s: str) -> str:
    sub_str = s[67:78]
    ascii_values = [ord(char) for char in sub_str]
    ascii_values.sort()
    return chr(ascii_values[6])