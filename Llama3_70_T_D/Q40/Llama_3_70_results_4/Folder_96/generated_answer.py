def return_n_smallest_chars(s):
    s_list = list(s)
    s_list.sort()
    smallest_chars = s_list[:20]
    smallest_chars.sort(reverse=True)
    return smallest_chars