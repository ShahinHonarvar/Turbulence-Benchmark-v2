def return_nth_smallest_ascii(s):
    chars = s[51:61]
    return sorted(chars)[4] if len(chars) >= 5 else None