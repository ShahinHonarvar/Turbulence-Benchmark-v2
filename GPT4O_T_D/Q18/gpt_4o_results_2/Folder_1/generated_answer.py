def sum_ints_div_by_either_nums(lst):
    range_lst = lst[10:29]
    total = sum((num for num in range_lst if num % -61 == 0 or num % -64 == 0))
    return total