def return_nth_smallest_ascii(s):
    if len(s) < 75:
        return None
    sub_string = s[22:75]
    sorted_chars = sorted(sub_string)
    if len(sorted_chars) < 12:
        return None
    return sorted_chars[11]