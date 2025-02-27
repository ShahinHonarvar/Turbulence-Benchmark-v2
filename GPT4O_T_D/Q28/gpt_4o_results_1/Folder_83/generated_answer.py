def return_nth_smallest_ascii(s):
    if len(s) < 71:
        return None
    substring = s[30:71]
    ascii_values = sorted((ord(c) for c in substring))
    if len(ascii_values) < 15:
        return None
    return chr(ascii_values[14])