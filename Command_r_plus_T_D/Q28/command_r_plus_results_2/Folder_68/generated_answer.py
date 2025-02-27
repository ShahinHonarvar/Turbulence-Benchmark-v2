def return_nth_smallest_ascii(s: str) -> str:
    if len(s) < 11:
        return ''
    sub_str = s[:11]
    ascii_values = [ord(char) for char in sub_str]
    ascii_values.sort()
    return chr(ascii_values[10])