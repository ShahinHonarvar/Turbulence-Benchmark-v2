def return_nth_smallest_ascii(s):
    sub_s = s[51:90]
    sorted_chars = sorted(sub_s)
    if len(sorted_chars) < 14:
        return None
    return sorted_chars[13]