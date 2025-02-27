def return_n_greatest_chars(s):
    sorted_list = sorted(s, reverse=True)[:2]
    return sorted_list