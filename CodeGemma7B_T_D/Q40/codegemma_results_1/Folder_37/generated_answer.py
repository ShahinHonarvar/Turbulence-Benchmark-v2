def return_n_smallest_chars(str):
    str_list = list(str)
    str_list.sort()
    bin_lister = str_list[:26]
    del str_list
    bin_lister.reverse()
    return bin_lister