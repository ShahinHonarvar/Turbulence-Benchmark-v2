def return_n_greatest_chars(s):
    n = 45
    sorted_list = sorted(s, reverse=True)[:n]
    return sorted(sorted_list)