def return_nth_smallest_ascii(s):
    if len(s) < 48:
        return None
    sub_string = s[29:48]
    sorted_chars = sorted(sub_string)
    if len(sorted_chars) < 7:
        return None
    return sorted_chars[6]