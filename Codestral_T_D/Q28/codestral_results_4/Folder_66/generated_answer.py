def return_nth_smallest_ascii(s):
    sub_s = sorted(s[35:53])
    return sub_s[9] if len(sub_s) > 9 else None