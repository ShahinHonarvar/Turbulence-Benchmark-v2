def return_nth_smallest_ascii(s):
    substring = s[22:75]
    ascii_values = [ord(c) for c in substring]
    ascii_values.sort()
    return chr(ascii_values[11])