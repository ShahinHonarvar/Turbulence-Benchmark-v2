def return_nth_smallest_ascii(s):
    if len(s) <= 59:
        return None
    sub_string = s[9:60]
    sorted_chars = sorted(sub_string)
    if len(sorted_chars) < 6:
        return None
    return sorted_chars[5]