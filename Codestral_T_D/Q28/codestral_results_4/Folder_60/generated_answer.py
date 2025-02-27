def return_nth_smallest_ascii(s):
    sub_s = sorted(s[36:80])
    return sub_s[11] if len(sub_s) > 11 else None