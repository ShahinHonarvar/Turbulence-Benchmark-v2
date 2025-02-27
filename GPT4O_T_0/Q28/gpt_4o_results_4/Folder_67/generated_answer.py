def return_nth_smallest_ascii(s):
    if len(s) < 84:
        return None
    sub_string = s[60:84]
    sorted_chars = sorted(sub_string)
    return sorted_chars[13] if len(sorted_chars) >= 14 else None