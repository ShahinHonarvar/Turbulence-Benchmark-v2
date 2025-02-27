def return_nth_smallest_ascii(s):
    sub_s = sorted(s[30:71])
    return sub_s[14] if len(sub_s) > 14 else None