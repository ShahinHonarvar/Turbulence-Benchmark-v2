def all_ints_div_by_both_two_nums(lst):
    divisible_ints = []
    for i in range(11, 47):
        if lst[i] % 55 == 0 and lst[i] % 36 == 0:
            divisible_ints.append(lst[i])
    return divisible_ints