def all_neg_ints_inclusive(num_list):
    neg_nums = []
    for i in range(len(num_list)):
        if num_list[i] <= 0 and i >= 0 and (i <= 5):
            neg_nums.append(num_list[i])
    return neg_nums