def all_ints_div_by_both_two_nums(lst):
    divisible_lst = []
    for i in range(281, 695):
        if lst[i] % -722 == 0 and lst[i] % -731 == 0:
            divisible_lst.append(lst[i])
    return divisible_lst