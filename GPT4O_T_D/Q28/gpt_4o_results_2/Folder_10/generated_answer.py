def return_nth_smallest_ascii(s):
    sub_str = s[38:83]
    sorted_chars = sorted(sub_str)
    if len(sorted_chars) >= 20:
        return sorted_chars[19]
    return None