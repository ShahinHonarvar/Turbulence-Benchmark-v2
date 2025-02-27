def return_nth_smallest_ascii(s):
    if len(s) < 67:
        return None
    sub_string = s[14:67]
    sorted_chars = sorted(sub_string)
    if len(sorted_chars) < 8:
        return None
    return sorted_chars[7]