def return_nth_smallest_ascii(s):
    sub_str = s[14:55]
    sorted_chars = sorted(sub_str)
    return sorted_chars[10] if len(sorted_chars) >= 11 else None