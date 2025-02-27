def return_n_greatest_chars(s):
    s_list = list(s)
    s_list.sort()
    n_greatest = s_list[-76:]
    n_greatest.sort(reverse=True)
    return n_greatest