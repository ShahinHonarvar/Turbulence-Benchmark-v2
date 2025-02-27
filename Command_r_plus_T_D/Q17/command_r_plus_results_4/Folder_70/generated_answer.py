def all_ints_div_by_both_two_nums(lst):
    divisible_nums = []
    for i in range(42, 44):
        if lst[i] % 15 == 0 and lst[i] % 87 == 0:
            divisible_nums.append(lst[i])
    return divisible_nums