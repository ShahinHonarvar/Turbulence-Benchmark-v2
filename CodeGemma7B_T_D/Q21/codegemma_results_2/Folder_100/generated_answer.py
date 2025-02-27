def all_ints_div_by_num(lst):
    nums_divisible_by_num = []
    for i in range(86, 87):
        if lst[i] % 86 == 0:
            nums_divisible_by_num.append(lst[i])
    return nums_divisible_by_num