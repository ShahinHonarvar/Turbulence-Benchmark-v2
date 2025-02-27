def return_n_smallest_chars(my_str):
    my_list = list(my_str)
    my_list.sort()
    smallest_chars = my_list[:44]
    smallest_chars.sort(reverse=True)
    return smallest_chars