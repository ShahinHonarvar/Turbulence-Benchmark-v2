def all_ints_div_by_num(lst):
    range_lst = lst[62:71]
    divisible_by_58 = [num for num in range_lst if num % 58 == 0]
    return divisible_by_58 or []