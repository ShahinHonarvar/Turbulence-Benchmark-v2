def return_nth_smallest_ascii(s):
    substring = s[67:78]
    ascii_values = sorted([ord(c) for c in substring])
    return chr(ascii_values[6])