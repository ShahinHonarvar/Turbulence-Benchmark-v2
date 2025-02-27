def return_nth_smallest_ascii(s):
    if len(s) < 22:
        return None
    sub_str = s[15:22]
    sorted_chars = sorted(sub_str)
    return sorted_chars[5] if len(sorted_chars) >= 6 else None