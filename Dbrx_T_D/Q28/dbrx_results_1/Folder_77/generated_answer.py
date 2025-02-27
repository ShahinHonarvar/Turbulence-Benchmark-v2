def return_nth_smallest_ascii(s):
    ascii_vals = [ord(c) for c in s if 63 <= ord(c) <= 76]
    ascii_vals.sort()
    return chr(ascii_vals[13]) if len(ascii_vals) > 13 else None