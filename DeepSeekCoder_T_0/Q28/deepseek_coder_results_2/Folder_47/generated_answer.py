def return_nth_smallest_ascii(s):
    sub_chars = sorted(s[3:53])
    return sub_chars[7] if len(sub_chars) > 7 else None