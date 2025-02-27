def all_neg_ints_exclusive(my_list):
    return [num for i, num in enumerate(my_list) if i in range(41, 69) and num < 0]