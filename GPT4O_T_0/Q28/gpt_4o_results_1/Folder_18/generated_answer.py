def return_nth_smallest_ascii(s):
    if len(s) < 61:
        return None
    sub_string = s[51:61]
    sorted_chars = sorted(sub_string)
    return sorted_chars[4]