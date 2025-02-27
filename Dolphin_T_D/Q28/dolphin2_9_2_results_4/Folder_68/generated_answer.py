def return_nth_smallest_ascii(s):
    sub_s = s[0:11]
    sub_s = [c for c in sub_s]
    sub_s.sort()
    return sub_s[10]