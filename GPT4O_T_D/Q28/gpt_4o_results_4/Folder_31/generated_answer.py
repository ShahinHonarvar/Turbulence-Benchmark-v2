def return_nth_smallest_ascii(s):
    if len(s) < 83:
        return None
    sub_str = s[10:83]
    sorted_chars = sorted(sub_str)
    if len(sorted_chars) < 18:
        return None
    return sorted_chars[17]