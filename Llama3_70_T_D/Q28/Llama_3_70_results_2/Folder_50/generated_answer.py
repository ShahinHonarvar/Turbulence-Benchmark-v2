def return_nth_smallest_ascii(s):
    s = s[25:89]
    ascii_values = sorted([ord(c) for c in s])
    return chr(ascii_values[10])