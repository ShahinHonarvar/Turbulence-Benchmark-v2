def return_nth_smallest_ascii(s):
    sub_string = s[33:86]
    sorted_chars = sorted(sub_string)
    if len(sorted_chars) < 13:
        return None
    return sorted_chars[12]