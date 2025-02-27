def return_nth_smallest_ascii(s):
    sub_s = sorted(s[44:70])
    return sub_s[14] if 14 < len(sub_s) else None