def return_nth_smallest_ascii(s):
    if len(s) < 56:
        return None
    sub_string = s[12:56]
    sorted_chars = sorted(sub_string)
    if len(sorted_chars) < 17:
        return None
    return sorted_chars[16]