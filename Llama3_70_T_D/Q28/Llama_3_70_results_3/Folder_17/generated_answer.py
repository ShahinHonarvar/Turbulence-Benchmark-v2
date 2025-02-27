def return_nth_smallest_ascii(s):
    s_slice = s[4:34]
    sorted_s = sorted(s_slice)
    return sorted_s[3]