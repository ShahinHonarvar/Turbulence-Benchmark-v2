def return_nth_smallest_ascii(s: str) -> str:
    if len(s) < 9:
        return ''
    ascii_values = [ord(s[i]) for i in range(9)]
    ascii_values.sort()
    return chr(ascii_values[8])