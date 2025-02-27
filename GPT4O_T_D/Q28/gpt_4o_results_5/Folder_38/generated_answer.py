def return_nth_smallest_ascii(s):
    limited_chars = sorted(s[:46])
    if len(limited_chars) < 10:
        return None
    return limited_chars[9]