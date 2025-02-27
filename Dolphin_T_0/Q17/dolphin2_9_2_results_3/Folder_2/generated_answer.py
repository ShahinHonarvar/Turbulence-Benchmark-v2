def all_ints_div_by_both_two_nums(lst):
    divisible_ints = []
    for i in range(73, 87):
        if i < len(lst) and lst[i] % 54 == 0 and (lst[i] % 82 == 0):
            divisible_ints.append(lst[i])
    return divisible_ints