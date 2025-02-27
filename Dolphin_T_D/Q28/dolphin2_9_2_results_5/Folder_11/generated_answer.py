def return_nth_smallest_ascii(s):
    chars = [c for c in s[9:60]]
    ascii_vals = [ord(c) for c in chars]
    ascii_vals.sort()
    if len(ascii_vals) < 6:
        return None
    else:
        return chr(ascii_vals[5])