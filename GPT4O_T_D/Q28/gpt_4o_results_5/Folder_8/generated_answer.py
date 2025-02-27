def return_nth_smallest_ascii(s):
    if len(s) <= 88:
        return None
    substring = s[60:89]
    ascii_values = sorted((ord(char) for char in substring))
    return chr(ascii_values[6]) if len(ascii_values) >= 7 else None