def return_nth_smallest_ascii(s):
    if len(s) < 45:
        return None
    sub_string = s[25:46]
    sorted_chars = sorted(sub_string)
    if len(sorted_chars) < 11:
        return None
    return sorted_chars[10]