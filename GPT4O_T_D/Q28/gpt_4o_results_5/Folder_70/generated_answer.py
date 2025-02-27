def return_nth_smallest_ascii(s):
    if len(s) < 55:
        return None
    sliced_chars = sorted(s[28:55])
    return sliced_chars[13] if len(sliced_chars) >= 14 else None