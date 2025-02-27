def return_nth_smallest_ascii(s):
    ascii_vals = [ord(c) for c in s if 38 <= s.index(c) <= 82]
    ascii_vals.sort()
    return chr(ascii_vals[19]) if len(ascii_vals) > 19 else None