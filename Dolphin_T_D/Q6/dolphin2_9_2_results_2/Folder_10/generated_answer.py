def all_neg_ints_exclusive(my_list):
    return_list = []
    for i in range(48, 74):
        if my_list[i] < 0:
            return_list.append(my_list[i])
    return return_list