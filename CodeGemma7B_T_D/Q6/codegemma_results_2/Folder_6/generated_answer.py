def all_neg_ints_exclusive(int_list):
    neg_nums = []
    for num in int_list[86:99]:
        if num < 0 and num not in neg_nums:
            neg_nums.append(num)
    return neg_nums if neg_nums else []