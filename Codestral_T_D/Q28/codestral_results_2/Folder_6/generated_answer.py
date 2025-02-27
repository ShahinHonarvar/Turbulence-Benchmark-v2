def return_nth_smallest_ascii(s):
    sub_s = sorted(s[14:55])
    return sub_s[10] if len(sub_s) > 10 else None