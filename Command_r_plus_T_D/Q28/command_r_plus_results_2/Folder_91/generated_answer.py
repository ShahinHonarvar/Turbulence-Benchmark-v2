def return_nth_smallest_ascii(s):
    s_list = list(s[:8])
    s_list.sort()
    return s_list[7]