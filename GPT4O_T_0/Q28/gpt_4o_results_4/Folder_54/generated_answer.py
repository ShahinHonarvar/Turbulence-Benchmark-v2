def return_nth_smallest_ascii(s):
    if len(s) < 88:
        return None
    sub_string = s[12:88]
    sorted_chars = sorted(sub_string)
    if len(sorted_chars) < 17:
        return None
    return sorted_chars[16]