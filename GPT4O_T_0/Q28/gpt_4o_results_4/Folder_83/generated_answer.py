def return_nth_smallest_ascii(s):
    if len(s) < 71:
        return None
    sub_string = s[30:71]
    sorted_chars = sorted(sub_string)
    if len(sorted_chars) < 15:
        return None
    return sorted_chars[14]