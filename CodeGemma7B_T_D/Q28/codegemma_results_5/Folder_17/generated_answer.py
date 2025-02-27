def return_nth_smallest_ascii(s):
    ascii_values = sorted([ord(c) for c in s[4:34] if ord(c) != ord(s[33])])
    if len(ascii_values) < 4:
        return None
    return chr(ascii_values[3])