def return_nth_smallest_ascii(s):
    sub = s[12:73]
    sorted_sub = sorted(sub, key=ord)
    return sorted_sub[12]