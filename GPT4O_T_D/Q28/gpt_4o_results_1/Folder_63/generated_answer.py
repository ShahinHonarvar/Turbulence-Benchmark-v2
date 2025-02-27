def return_nth_smallest_ascii(s):
    if len(s) < 71:
        return None
    sub_string = s[47:71]
    unique_chars_in_sub = sorted(set(sub_string))
    if len(unique_chars_in_sub) < 14:
        return None
    return unique_chars_in_sub[13]