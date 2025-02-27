def return_nth_smallest_ascii(s):
    if len(s) < 60:
        return None
    sub_string = s[42:60]
    sorted_chars = sorted(sub_string)
    if len(sorted_chars) < 17:
        return None
    return sorted_chars[16]