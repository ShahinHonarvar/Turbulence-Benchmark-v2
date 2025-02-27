def return_nth_smallest_ascii(s):
    sub_str_chars = sorted(list(s[14:55]))
    return sub_str_chars[10] if len(sub_str_chars) >= 11 else None