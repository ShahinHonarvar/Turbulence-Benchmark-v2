def return_n_smallest_chars(s):
    s = list(s)
    s.sort()
    return_list = s[:59]
    return_list.sort(reverse=True)
    return return_list