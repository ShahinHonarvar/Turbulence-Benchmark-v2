def return_nth_smallest_ascii(s):
    if len(s) < 59:
        return None
    sub_str = s[6:59]
    sorted_chars = sorted(sub_str)
    return sorted_chars[18] if len(sorted_chars) >= 19 else None