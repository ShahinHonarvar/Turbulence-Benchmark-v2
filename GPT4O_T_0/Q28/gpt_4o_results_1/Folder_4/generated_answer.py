def return_nth_smallest_ascii(s):
    if len(s) < 23:
        return None
    sub_string = s[9:23]
    sorted_chars = sorted(sub_string)
    return sorted_chars[3]