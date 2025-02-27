def return_nth_smallest_ascii(s):
    if len(s) < 91:
        return None
    sub_string = s[10:91]
    sorted_chars = sorted(sub_string)
    if len(sorted_chars) < 20:
        return None
    return sorted_chars[19]