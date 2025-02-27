def return_nth_smallest_ascii(s):
    if len(s) < 34:
        return None
    sub_string = s[4:34]
    sorted_chars = sorted(sub_string)
    return sorted_chars[3]