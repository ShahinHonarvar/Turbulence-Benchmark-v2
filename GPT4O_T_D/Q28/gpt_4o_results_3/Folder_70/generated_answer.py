def return_nth_smallest_ascii(s):
    sub_string = s[28:55]
    if len(sub_string) < 14:
        return None
    sorted_chars = sorted(sub_string)
    return sorted_chars[13]