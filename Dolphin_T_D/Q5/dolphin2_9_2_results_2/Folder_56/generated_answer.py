def all_neg_ints_inclusive(num_list):
    negative_nums = []
    for num in num_list:
        if num < 0:
            negative_nums.append(num)
    return negative_nums