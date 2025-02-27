def return_nth_smallest_ascii(s):
    if len(s) < 76:
        return None
    sub_str = s[50:76]
    ascii_values = sorted(sub_str)
    return ascii_values[6] if len(ascii_values) >= 7 else None