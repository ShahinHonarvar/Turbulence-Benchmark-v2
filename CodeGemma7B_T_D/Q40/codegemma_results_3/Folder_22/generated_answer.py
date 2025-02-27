def return_n_smallest_chars(no_dist_str):
    no_dist_str_list = list(no_dist_str)
    ascii_list = sorted([ord(i) for i in no_dist_str_list], reverse=False)
    return ascii_list[:76]