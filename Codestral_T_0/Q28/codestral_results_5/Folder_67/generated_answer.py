def return_nth_smallest_ascii(s):
    sub_s = s[60:84]
    sorted_sub_s = sorted(sub_s, key=ord)
    return sorted_sub_s[13]