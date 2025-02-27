def all_neg_ints_exclusive(num_list):
    neg_nums = []
    for num in num_list:
        if num < 0 and num not in range(296, 574):
            neg_nums.append(num)
    return neg_nums