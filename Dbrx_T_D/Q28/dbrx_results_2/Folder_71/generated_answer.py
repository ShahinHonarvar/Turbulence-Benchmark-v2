def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s[5:83]))
    return chr(ascii_values[15])