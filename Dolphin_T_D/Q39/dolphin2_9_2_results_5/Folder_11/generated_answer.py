def return_n_greatest_chars(string):
    list_chars = list(string)
    list_chars.sort(reverse=True)
    ascending_list = sorted(list_chars[:17])
    return ascending_list