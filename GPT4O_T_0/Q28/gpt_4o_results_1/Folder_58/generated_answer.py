def return_nth_smallest_ascii(s):
    if len(s) < 27:
        return None
    sub_string = s[8:27]
    sorted_chars = sorted(sub_string)
    return sorted_chars[5] if len(sorted_chars) >= 6 else None