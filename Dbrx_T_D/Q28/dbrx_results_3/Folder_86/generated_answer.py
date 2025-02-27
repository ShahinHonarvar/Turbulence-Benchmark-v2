def return_nth_smallest_ascii(s):
    sub_s = s[44:70]
    ascii_values = sorted(set((ord(c) for c in sub_s)))
    return chr(ascii_values[14]) if len(ascii_values) > 14 else None