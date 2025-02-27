def return_n_greatest_chars(s):
    sorted_list = sorted(s, reverse=True)[:31]
    return sorted(sorted_list)