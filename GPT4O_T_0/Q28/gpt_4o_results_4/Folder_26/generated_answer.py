def return_nth_smallest_ascii(s):
    if len(s) < 37:
        return None
    sub_string = s[1:37]
    sorted_chars = sorted(sub_string)
    return sorted_chars[14] if len(sorted_chars) >= 15 else None