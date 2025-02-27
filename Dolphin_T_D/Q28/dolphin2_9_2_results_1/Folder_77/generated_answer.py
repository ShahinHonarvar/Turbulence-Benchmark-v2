def return_nth_smallest_ascii(s):
    substring = s[63:77]
    ascii_values = sorted([ord(c) for c in substring if c != ''])
    return chr(ascii_values[13])