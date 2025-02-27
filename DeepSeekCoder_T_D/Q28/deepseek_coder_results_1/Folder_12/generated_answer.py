def return_nth_smallest_ascii(s):
    sub_chars = sorted(s[3:27])
    return sub_chars[4] if len(sub_chars) > 4 else None