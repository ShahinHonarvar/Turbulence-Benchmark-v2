def return_nth_smallest_ascii(s):
    if len(s) < 27:
        return None
    sub_string = s[8:27]
    sorted_chars = sorted(sub_string, key=ord)
    if len(sorted_chars) < 6:
        return None
    return sorted_chars[5]