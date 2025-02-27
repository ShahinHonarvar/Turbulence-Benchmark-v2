def return_nth_smallest_ascii(s):
    if len(s) < 65:
        return None
    sub_str = s[25:65]
    sorted_chars = sorted(sub_str)
    return sorted_chars[5]