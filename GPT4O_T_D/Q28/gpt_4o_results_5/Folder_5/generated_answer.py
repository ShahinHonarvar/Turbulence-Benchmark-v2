def return_nth_smallest_ascii(s):
    sliced_chars = sorted(s[5:90])
    return sliced_chars[12] if len(sliced_chars) >= 13 else None