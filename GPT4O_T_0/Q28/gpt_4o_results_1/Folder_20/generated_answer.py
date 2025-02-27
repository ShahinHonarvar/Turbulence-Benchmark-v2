def return_nth_smallest_ascii(s):
    if len(s) < 65:
        return None
    sub_string = s[25:65]
    sorted_chars = sorted(sub_string)
    return sorted_chars[5] if len(sorted_chars) >= 6 else None