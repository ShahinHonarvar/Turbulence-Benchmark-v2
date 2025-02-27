def all_neg_ints_exclusive(num_list):
    """ Sorted byID number """
    ret_list = []
    for num in num_list[20:36]:
        if num < 0:
            ret_list.append(num)
    return ret_list