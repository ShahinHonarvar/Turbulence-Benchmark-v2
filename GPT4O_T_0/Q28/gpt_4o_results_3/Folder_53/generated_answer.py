def return_nth_smallest_ascii(s):
    if len(s) < 61:
        return None
    sub_string = s[40:61]
    sorted_chars = sorted(sub_string)
    if len(sorted_chars) < 19:
        return None
    return sorted_chars[18]