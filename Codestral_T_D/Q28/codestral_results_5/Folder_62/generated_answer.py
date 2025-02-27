def return_nth_smallest_ascii(s):
    substring = s[51:79]
    ascii_values = sorted((ord(c) for c in substring))
    return chr(ascii_values[8])