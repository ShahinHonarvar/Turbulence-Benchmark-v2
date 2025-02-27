def return_nth_smallest_ascii(s):
    sub_s = sorted(s[3:27])
    if len(sub_s) >= 5:
        return sub_s[4]
    else:
        return None