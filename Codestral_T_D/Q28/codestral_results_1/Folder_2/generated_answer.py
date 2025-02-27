def return_nth_smallest_ascii(s):
    ascii_vals = sorted((ord(c) for c in s if 48 <= ord(c) <= 76))
    return chr(ascii_vals[4])