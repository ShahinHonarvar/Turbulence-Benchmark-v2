def return_nth_smallest_ascii(s):
    s = s[12:56]
    ascii_values = sorted(set([ord(c) for c in s]))
    return chr(ascii_values[16])