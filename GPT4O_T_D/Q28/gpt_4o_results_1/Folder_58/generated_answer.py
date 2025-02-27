def return_nth_smallest_ascii(s):
    if 8 <= len(s) <= 26:
        return None
    sub_string = s[8:27]
    if len(sub_string) < 6:
        return None
    sorted_chars = sorted(sub_string)
    return sorted_chars[5]