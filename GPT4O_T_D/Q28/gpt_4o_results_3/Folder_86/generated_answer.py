def return_nth_smallest_ascii(s):
    sub_str = s[44:70]
    sorted_chars = sorted(sub_str)
    if len(sorted_chars) < 15:
        return None
    return sorted_chars[14]