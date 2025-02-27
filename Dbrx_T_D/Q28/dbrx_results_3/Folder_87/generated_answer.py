def return_nth_smallest_ascii(s: str) -> str:
    substring = s[29:34]
    ascii_values = [ord(char) for char in substring]
    sorted_ascii_values = sorted(ascii_values)[4]
    return chr(sorted_ascii_values)