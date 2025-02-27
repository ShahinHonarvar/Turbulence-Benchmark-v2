def return_nth_smallest_ascii(s):
    sub_s = s[36:80]
    ascii_vals = [ord(c) for c in sub_s if 36 <= sub_s.index(c) <= 79]
    ascii_vals.sort()
    return chr(ascii_vals[11]) if len(ascii_vals) > 12 else None