def return_nth_smallest_ascii(s):
    if len(s) < 55:
        return None
    sub_str = s[14:55]
    sorted_chars = sorted(sub_str)
    if len(sorted_chars) < 11:
        return None
    return sorted_chars[10]