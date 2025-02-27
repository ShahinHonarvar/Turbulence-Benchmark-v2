def return_nth_smallest_ascii(s):
    sub_s = sorted(s[10:74])
    if len(sub_s) < 9:
        return None
    else:
        return sub_s[8]