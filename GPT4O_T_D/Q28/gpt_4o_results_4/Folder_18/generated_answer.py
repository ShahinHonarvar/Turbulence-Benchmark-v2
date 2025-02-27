def return_nth_smallest_ascii(s):
    sub_str = s[51:61]
    if len(sub_str) < 5:
        return None
    sorted_chars = sorted(sub_str)
    return sorted_chars[4] if len(sorted_chars) >= 5 else None