def return_nth_smallest_ascii(s):
    if len(s) < 60:
        return None
    sub_s = s[9:60]
    sorted_chars = sorted(sub_s)
    if len(sorted_chars) < 6:
        return None
    return sorted_chars[5]