def return_nth_smallest_ascii(s):
    sub_str = s[50:77]
    sorted_chars = sorted(sub_str)
    if len(sorted_chars) < 11:
        return None
    return sorted_chars[10]