def return_nth_smallest_ascii(s):
    sub_chars = sorted(s[5:83])
    return sub_chars[15] if len(sub_chars) > 15 else None