def return_nth_smallest_ascii(s):
    sub_str = s[40:61]
    sorted_chars = sorted(sub_str)
    return sorted_chars[18] if len(sorted_chars) >= 19 else None