def return_nth_smallest_ascii(s):
    if len(s) < 61:
        return None
    sub_str = s[51:61]
    sorted_chars = sorted(sub_str)
    return sorted_chars[4] if len(sorted_chars) >= 5 else None