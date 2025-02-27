def all_ints_div_by_both_two_nums(lst):
    divisible_nums = []
    for i in range(2):
        if lst[i] % -6 == 0 and lst[i] % 4 == 0:
            divisible_nums.append(lst[i])
    return divisible_nums