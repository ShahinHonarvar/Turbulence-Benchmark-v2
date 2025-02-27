def return_nth_smallest_ascii(s):
    if len(s) < 82:
        return None
    sub_string = s[34:82]
    sorted_chars = sorted(sub_string)
    if len(sorted_chars) < 12:
        return None
    return sorted_chars[11]