def return_nth_smallest_ascii(s):
    sub_str = s[17:57]
    sorted_chars = sorted(sub_str)
    return sorted_chars[8] if len(sorted_chars) > 8 else None