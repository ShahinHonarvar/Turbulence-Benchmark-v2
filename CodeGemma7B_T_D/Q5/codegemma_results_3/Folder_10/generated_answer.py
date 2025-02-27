def all_neg_ints_inclusive(list_of_ints):
    negative_nums = []
    for num in list_of_ints[25:60]:
        if num < 0:
            negative_nums.append(num)
    return negative_nums