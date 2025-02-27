def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[28:68]
    ascii_values = [ord(char) for char in sub_s]
    ascii_values.sort()
    return chr(ascii_values[14])