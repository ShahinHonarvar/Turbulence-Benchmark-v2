def return_nth_smallest_ascii(s):
    sub_s = s[8:66]
    sorted_sub_s = sorted(sub_s)
    if len(sorted_sub_s) >= 6:
        return sorted_sub_s[5]
    else:
        return None