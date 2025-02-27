def return_nth_smallest_ascii(s):
    sub_str = s[50:76]
    sorted_chars = sorted(sub_str)
    if len(sorted_chars) < 7:
        return None
    return sorted_chars[6]