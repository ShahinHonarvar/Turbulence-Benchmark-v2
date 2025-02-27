def return_nth_smallest_ascii(s):
    sub_chars = sorted(s[1:32])
    return sub_chars[5] if len(sub_chars) >= 6 else None