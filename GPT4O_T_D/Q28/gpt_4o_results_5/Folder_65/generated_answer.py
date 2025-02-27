def return_nth_smallest_ascii(s):
    target_chars = sorted(s[32:68])
    if len(target_chars) < 12:
        return None
    return target_chars[11]