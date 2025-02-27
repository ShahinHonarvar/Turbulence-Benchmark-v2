def all_ints_div_by_both_two_nums(lst):
    desired_nums = []
    for i in range(18, 53):
        if i < len(lst):
            if lst[i] % 15 == 0 and lst[i] % 57 == 0:
                desired_nums.append(lst[i])
    return desired_nums