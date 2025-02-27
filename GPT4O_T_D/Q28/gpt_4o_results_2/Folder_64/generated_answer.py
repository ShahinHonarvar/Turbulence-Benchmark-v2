def return_nth_smallest_ascii(s):
    if len(s) < 7:
        return None
    sub_s = s[:7]
    sorted_sub_s = sorted(sub_s)
    return sorted_sub_s[6]