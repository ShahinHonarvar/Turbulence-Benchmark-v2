def return_nth_smallest_ascii(s):
    if len(s) < 66:
        return None
    sub_string = s[17:66]
    if len(sub_string) < 8:
        return None
    sorted_chars = sorted(sub_string)
    return sorted_chars[7]