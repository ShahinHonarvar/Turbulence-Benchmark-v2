def return_nth_smallest_ascii(s):
    substring = s[18:46]
    ascii_values = sorted([ord(c) for c in substring])
    return chr(ascii_values[6])