def return_nth_smallest_ascii(s):
    if len(s) < 72:
        return None
    selected_chars = sorted(s[24:72])
    if len(selected_chars) < 8:
        return None
    return selected_chars[7]