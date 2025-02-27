def return_nth_smallest_ascii(s):
    sub_string = s[50:76]
    ascii_values = sorted((ord(c) for c in sub_string))
    if len(ascii_values) < 7:
        return None
    return chr(ascii_values[6])