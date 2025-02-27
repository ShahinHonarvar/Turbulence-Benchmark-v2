def return_nth_smallest_ascii(s):
    if len(s) < 78:
        return None
    sub_string = s[25:78]
    sorted_chars = sorted(sub_string)
    return sorted_chars[15] if len(sorted_chars) >= 16 else None