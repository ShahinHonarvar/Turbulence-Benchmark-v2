def return_nth_smallest_ascii(s):
    ascii_vals = sorted((ord(c) for c in s[50:77] if c.isalpha()))
    if len(ascii_vals) >= 11:
        return chr(ascii_vals[10])
    else:
        return None