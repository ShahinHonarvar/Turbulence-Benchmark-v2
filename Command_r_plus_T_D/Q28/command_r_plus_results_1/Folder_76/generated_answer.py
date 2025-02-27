def return_nth_smallest_ascii(s: str) -> str:
    if len(s) < 67:
        return ''
    sub_str = s[18:67]
    ascii_values = sorted((ord(char) for char in sub_str))
    return chr(ascii_values[18])