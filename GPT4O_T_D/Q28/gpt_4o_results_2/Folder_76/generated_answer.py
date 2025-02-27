def return_nth_smallest_ascii(s):
    sub_str = s[18:67]
    sorted_chars = sorted(sub_str)
    return sorted_chars[18] if len(sorted_chars) >= 19 else None