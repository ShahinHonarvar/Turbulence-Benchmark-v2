def return_nth_smallest_ascii(s):
    if len(s) < 34:
        return None
    sub_str = s[29:34]
    sorted_chars = sorted(sub_str)
    return sorted_chars[4] if len(sorted_chars) >= 5 else None