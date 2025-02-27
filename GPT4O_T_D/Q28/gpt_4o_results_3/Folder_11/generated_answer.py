def return_nth_smallest_ascii(s):
    sub_str = s[9:60]
    sorted_chars = sorted(sub_str)
    return sorted_chars[5] if len(sorted_chars) >= 6 else None