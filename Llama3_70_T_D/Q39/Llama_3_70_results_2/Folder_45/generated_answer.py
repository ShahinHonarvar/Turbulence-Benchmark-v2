def return_n_greatest_chars(s):
    sorted_list = sorted(s)[-52:]
    sorted_list.sort()
    return sorted_list