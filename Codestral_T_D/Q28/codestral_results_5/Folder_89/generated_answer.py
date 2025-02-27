def return_nth_smallest_ascii(s):
    sub_str = s[24:72]
    sorted_chars = sorted(sub_str)
    return sorted_chars[7] if len(sorted_chars) > 7 else None