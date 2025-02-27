def all_neg_ints_exclusive(num_list):
    neg_nums = []
    for num in num_list[369:983]:
        if num < 0:
            neg_nums.append(num)
    return neg_nums