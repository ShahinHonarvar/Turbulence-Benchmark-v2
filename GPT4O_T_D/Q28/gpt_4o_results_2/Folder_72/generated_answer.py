def return_nth_smallest_ascii(s):
    sub_str = s[33:61]
    sorted_chars = sorted(sub_str)
    return sorted_chars[17] if len(sorted_chars) > 17 else None