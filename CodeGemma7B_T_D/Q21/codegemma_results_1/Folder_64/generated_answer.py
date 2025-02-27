def all_ints_div_by_num(lst_nums):
    return [num for num in lst_nums if num % 4 == 0 and num >= 0 and (num <= lst_nums[-1])]