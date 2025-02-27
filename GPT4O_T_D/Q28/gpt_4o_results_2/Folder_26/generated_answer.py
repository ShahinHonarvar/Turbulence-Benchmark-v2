def return_nth_smallest_ascii(s):
    if len(s) < 37:
        return None
    sub_str = s[1:37]
    sorted_chars = sorted(sub_str)
    return sorted_chars[14]