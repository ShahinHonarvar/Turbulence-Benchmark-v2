def return_nth_smallest_ascii(s):
    if len(s) < 82:
        return None
    sub_string = s[34:82]
    sorted_chars = sorted(sub_string)
    return sorted_chars[11] if len(sorted_chars) >= 12 else None