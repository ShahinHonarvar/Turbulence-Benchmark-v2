def return_nth_smallest_ascii(s):
    sub_s = s[46:73]
    sorted_sub_s = sorted(set(sub_s), key=lambda c: ord(c))
    return sorted_sub_s[14]