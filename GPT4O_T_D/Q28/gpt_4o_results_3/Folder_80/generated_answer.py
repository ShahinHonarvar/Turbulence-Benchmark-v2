def return_nth_smallest_ascii(s):
    if len(s) < 90:
        return ''
    sub_str = s[51:90]
    sorted_chars = sorted(sub_str)
    return sorted_chars[13] if len(sorted_chars) > 13 else ''