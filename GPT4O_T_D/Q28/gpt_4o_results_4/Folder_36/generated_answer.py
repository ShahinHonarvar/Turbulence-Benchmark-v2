def return_nth_smallest_ascii(s):
    if len(s) < 57:
        return None
    sub_string = s[17:57]
    ascii_values = sorted([ord(char) for char in sub_string])
    return chr(ascii_values[8]) if len(ascii_values) >= 9 else None