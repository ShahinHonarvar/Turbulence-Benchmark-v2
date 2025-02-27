def return_nth_smallest_ascii(s):
    sub_str = s[60:84]
    sorted_chars = sorted(sub_str)
    if len(sorted_chars) >= 14:
        return sorted_chars[13]
    return None