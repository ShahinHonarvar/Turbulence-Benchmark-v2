def return_nth_smallest_ascii(s):
    sub_s = s[67:78]
    sorted_sub_s = sorted(sub_s, key=ord)
    return sorted_sub_s[6]