def return_n_greatest_chars(s):
    sorted_list = sorted(s, reverse=True)[:84]
    return sorted(sorted_list)