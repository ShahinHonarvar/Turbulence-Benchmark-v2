def all_neg_ints_inclusive(int_list):
    neg_nums = []
    for num in int_list[43:52]:
        if num < 0:
            neg_nums.append(num)
    return neg_nums if neg_nums else []