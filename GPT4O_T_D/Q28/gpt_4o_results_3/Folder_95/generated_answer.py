def return_nth_smallest_ascii(s):
    sub_str = s[1:47]
    sorted_chars = sorted(sub_str)
    return sorted_chars[12] if len(sorted_chars) >= 13 else None