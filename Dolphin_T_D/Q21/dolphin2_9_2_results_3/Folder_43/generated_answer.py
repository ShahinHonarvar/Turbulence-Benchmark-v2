def all_ints_div_by_num(lst):
    range_lst = lst[10:38]
    divisible_lst = [num for num in range_lst if num % -64 == 0]
    return divisible_lst