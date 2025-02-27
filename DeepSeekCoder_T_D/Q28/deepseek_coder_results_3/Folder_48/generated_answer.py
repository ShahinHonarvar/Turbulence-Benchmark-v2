def return_nth_smallest_ascii(s):
    sub_str = s[37:60]
    sorted_chars = sorted(sub_str)
    return sorted_chars[5] if len(sorted_chars) > 5 else None