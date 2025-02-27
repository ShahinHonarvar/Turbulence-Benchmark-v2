def return_nth_smallest_ascii(s):
    sub_s = sorted(s[50:76])
    return sub_s[6] if len(sub_s) > 6 else None