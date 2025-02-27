def return_nth_smallest_ascii(s):
    if len(s) < 76:
        return None
    sub_string = s[50:76]
    sorted_chars = sorted(sub_string)
    if len(sorted_chars) < 7:
        return None
    return sorted_chars[6]