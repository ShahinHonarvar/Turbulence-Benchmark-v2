def return_nth_smallest_ascii(s):
    if len(s) < 90:
        return None
    sub_string = s[51:90]
    sorted_chars = sorted(sub_string)
    return sorted_chars[13] if len(sorted_chars) >= 14 else None