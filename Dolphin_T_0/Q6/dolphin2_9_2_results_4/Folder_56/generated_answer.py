def all_neg_ints_exclusive(num_list):
    neg_nums = []
    for i in range(8, 10):
        if num_list[i] < 0:
            neg_nums.append(num_list[i])
    return neg_nums