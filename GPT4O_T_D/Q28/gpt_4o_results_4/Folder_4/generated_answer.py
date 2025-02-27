def return_nth_smallest_ascii(s):
    if len(s) < 23:
        return None
    sub_string = s[9:23]
    sorted_chars = sorted(sub_string)
    if len(sorted_chars) < 4:
        return None
    return sorted_chars[3]