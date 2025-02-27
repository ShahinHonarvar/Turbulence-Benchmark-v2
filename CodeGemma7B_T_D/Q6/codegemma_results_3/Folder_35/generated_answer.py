def all_neg_ints_exclusive(int_list):
    filtered_nums = []
    for i in range(10, 79):
        if int_list[i] < 0:
            filtered_nums.append(int_list[i])
    return filtered_nums if filtered_nums else []