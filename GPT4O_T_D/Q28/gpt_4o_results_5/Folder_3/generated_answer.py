def return_nth_smallest_ascii(s):
    if not s or len(s) < 46:
        return None
    sub_str = s[25:46]
    if len(sub_str) < 21:
        return None
    sorted_chars = sorted(sub_str)
    return sorted_chars[10]