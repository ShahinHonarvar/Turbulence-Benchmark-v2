def return_nth_smallest_ascii(s):
    sub_s = sorted(s[4:34])
    if len(sub_s) >= 4:
        return sub_s[3]
    else:
        return None